#!/usr/bin/env python3
"""Install the overlay, then build a downstream CMake consumer with vcpkg."""
import argparse
from pathlib import Path
import shutil
import subprocess
import zipfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--vcpkg', type=Path, required=True)
parser.add_argument('--overlay', type=Path, default=ROOT / 'ports')
parser.add_argument('--release', action='store_true', help='test the generated standalone release overlay')
args = parser.parse_args()
vcpkg = args.vcpkg.resolve()
with tempfile.TemporaryDirectory(prefix='supertest-vcpkg-install-') as temporary:
    base = Path(temporary)
    installed = base / 'installed'
    overlay = args.overlay.resolve()
    if args.release:
        version = (ROOT / 'VERSION').read_text().strip()
        overlay = base / 'overlay'
        with zipfile.ZipFile(ROOT / 'dist' / f'schematic-supertest-vcpkg-{version}.zip') as archive:
            archive.extractall(overlay)
        # The future public URL is intentionally not live yet. Seed vcpkg's
        # download cache with the exact asset; the generated port still verifies
        # its SHA512 through vcpkg_download_distfile.
        source = ROOT / 'dist' / f'supertest-c-{version}.tar.gz'
        downloads = vcpkg.parent / 'downloads'
        downloads.mkdir(exist_ok=True)
        shutil.copyfile(source, downloads / source.name)
    subprocess.run([str(vcpkg), 'install', 'schematic-supertest', '--triplet=x64-linux',
                    f'--overlay-ports={overlay}', f'--x-install-root={installed}', '--binarysource=clear'], check=True)
    build = base / 'consumer'
    subprocess.run(['cmake', '-S', str(ROOT / 'tests/consumer'), '-B', str(build),
                    f'-DCMAKE_TOOLCHAIN_FILE={vcpkg.parent}/scripts/buildsystems/vcpkg.cmake',
                    f'-DVCPKG_INSTALLED_DIR={installed}', '-DVCPKG_TARGET_TRIPLET=x64-linux'], check=True)
    subprocess.run(['cmake', '--build', str(build)], check=True)
    subprocess.run(['ctest', '--test-dir', str(build), '--output-on-failure'], check=True)
print('vcpkg overlay and downstream consumer passed')
