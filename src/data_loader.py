import pandas as pd
from pathlib import Path


class DataLoader:
    def __init__(self, data_path: str):
        """
        Initializes the DataLoader with the given data path.

        Args:
            data_path (str): Path to the dataset file.
        """
        self.data_path = Path(data_path)

    def load_data(self, sep: str = "|") -> pd.DataFrame:
        """
        Loads the dataset from the specified path.

        Args:
            sep (str): Separator used in the dataset file.

        Returns:
            pd.DataFrame: Loaded dataset.
        """
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found at: {self.data_path}")
        self.df = pd.read_csv(self.data_path, sep=sep)
        return self.df

    def summarize_data(self):
        if self.df is not None:
            print("Data Summary:")
            print(self.df.describe())
            print(self.df.info())
            print(self.df.isnull().sum())
        else:
            print("No data loaded!")
