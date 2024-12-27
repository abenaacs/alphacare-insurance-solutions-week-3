import os
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Visualizer:
    def __init__(self, df: pd.DataFrame, output_dir: str):
        self.df = df
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def plot_histograms(self, numeric_columns):
        for column in numeric_columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df[column], kde=True, bins=30, color="blue")
            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            file_path = self.output_dir / f"histogram_{column}.png"
            plt.savefig(file_path, dpi=300, bbox_inches="tight")
            plt.close()

    def plot_correlation_heatmap(self, numeric_columns):
        correlation = self.df[numeric_columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        file_path = self.output_dir / "correlation_heatmap.png"
        plt.savefig(file_path, dpi=300, bbox_inches="tight")
        plt.close()
