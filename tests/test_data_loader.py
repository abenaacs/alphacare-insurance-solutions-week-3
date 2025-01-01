import unittest
from scripts.data_loader import DataLoader
from pathlib import Path
import pandas as pd


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.valid_path = "test_data/test_file.txt"
        self.invalid_path = "invalid/path/to/file.txt"
        Path("test_data").mkdir(exist_ok=True)
        with open(self.valid_path, "w") as f:
            f.write("Column1|Column2|Column3\n1|2|3\n4|5|6\n")

    def tearDown(self):
        if Path(self.valid_path).exists():
            Path(self.valid_path).unlink()
        if Path("test_data").exists():
            Path("test_data").rmdir()

    def test_load_data_valid_path(self):
        loader = DataLoader(self.valid_path)
        df = loader.load_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)

    def test_load_data_invalid_path(self):
        loader = DataLoader(self.invalid_path)
        with self.assertRaises(FileNotFoundError):
            loader.load_data()


if __name__ == "__main__":
    unittest.main()
