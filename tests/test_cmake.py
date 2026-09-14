"""Test vendoring and discovery after relocating a CMake installation."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run(args, check=True)


class CMakeTests(unittest.TestCase):
    def test_vendored_and_relocated_install(self):
        with tempfile.TemporaryDirectory(prefix="supertest-cmake-") as temporary:
            base = Path(temporary)
            installed = base / "original"
            moved = base / "relocated"
            run("cmake", "-S", str(ROOT), "-B", str(base / "library"),
                "-DSUPERTEST_BUILD_TESTS=ON", f"-DCMAKE_INSTALL_PREFIX={installed}")
            run("cmake", "--build", str(base / "library"), "--config", "Release")
            run("ctest", "--test-dir", str(base / "library"), "-C", "Release", "--output-on-failure")
            run("cmake", "--install", str(base / "library"), "--config", "Release")
            installed.rename(moved)
            for mode, option in (("installed", f"-DCMAKE_PREFIX_PATH={moved}"),
                                 ("vendored", f"-DSUPERTEST_SOURCE={ROOT}")):
                build = base / mode
                run("cmake", "-S", str(ROOT / "tests/consumer"), "-B", str(build), option)
                run("cmake", "--build", str(build), "--config", "Release")
                run("ctest", "--test-dir", str(build), "-C", "Release", "--output-on-failure")
            self.assertTrue((moved / "include/schematic.h").is_file())


if __name__ == "__main__":
    unittest.main()
