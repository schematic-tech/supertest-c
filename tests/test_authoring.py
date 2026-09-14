"""Check process status and continuation independently of the C process."""
import os
import subprocess
import unittest


class AuthoringTests(unittest.TestCase):
    def run_probe(self, mode):
        return subprocess.run(
            [os.environ.get("SUPERTEST_C_EXECUTABLE", "./build/authoring"), mode], capture_output=True, text=True, timeout=10
        )

    def test_true_continues(self):
        result = self.run_probe("true")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), ["entered", "continued"])

    def test_false_exits_successfully_from_nested_helper(self):
        result = self.run_probe("false")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), ["entered"])
        self.assertEqual(result.stderr, "")

    def test_assertion_still_fails(self):
        result = self.run_probe("assertion")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ordinary assertion failure", result.stderr)


if __name__ == "__main__":
    unittest.main()
