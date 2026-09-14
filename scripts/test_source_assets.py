#!/usr/bin/env python3
"""Consume the actual source release through CMake FetchContent."""
from pathlib import Path
import hashlib
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / 'VERSION').read_text().strip()
source = ROOT / 'dist' / f'supertest-c-{version}.tar.gz'
with tempfile.TemporaryDirectory(prefix='supertest-fetch-') as temporary:
    build = Path(temporary) / 'build'
    subprocess.run(['cmake', '-S', str(ROOT / 'tests/consumer'), '-B', str(build),
                    f'-DSUPERTEST_ARCHIVE={source.as_uri()}',
                    f'-DSUPERTEST_ARCHIVE_SHA256={hashlib.sha256(source.read_bytes()).hexdigest()}'], check=True)
    subprocess.run(['cmake', '--build', str(build)], check=True)
    subprocess.run(['ctest', '--test-dir', str(build), '--output-on-failure'], check=True)
with zipfile.ZipFile(ROOT / 'dist' / f'schematic-supertest-vcpkg-{version}.zip') as overlay:
    port = overlay.read('schematic-supertest/portfile.cmake').decode()
    assert hashlib.sha512(source.read_bytes()).hexdigest() in port
    assert f'/releases/download/v{version}/{source.name}' in port
print('Source archive and release vcpkg overlay are ready')
