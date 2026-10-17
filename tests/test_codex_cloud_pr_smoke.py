import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CodexCloudPRSmokeTests(unittest.TestCase):
    def test_gitignore_exists(self):
        self.assertTrue((ROOT / ".gitignore").is_file())

    def test_mainline_entry_files_exist(self):
        for name in ("README.md", "bootstrap.py"):
            with self.subTest(name=name):
                self.assertTrue((ROOT / "mainline_v33" / name).is_file())

    def test_upload_parts_exist_and_are_nonempty(self):
        for index in range(11):
            path = ROOT / "upload_parts" / f"part_{index:03d}.txt"
            with self.subTest(part=path.name):
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
