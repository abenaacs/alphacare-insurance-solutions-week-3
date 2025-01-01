# test_visualizer.py: Test cases for Visualizer
import unittest
import pandas as pd
from scripts.visualizer import Visualizer
from pathlib import Path


class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_visualizations"
        Path(self.output_dir).mkdir(exist_ok=True)
        data = {"Column1": [1, 2, 3, 4], "Column2": [5, 6, 7, 8]}
        self.df = pd.DataFrame(data)

    def tearDown(self):
        if Path(self.output_dir).exists():
            for file in Path(self.output_dir).glob("*"):
                file.unlink()
            Path(self.output_dir).rmdir()

    def test_plot_histograms(self):
        visualizer = Visualizer(self.df, self.output_dir)
        visualizer.plot_histograms(["Column1", "Column2"])
        self.assertTrue(Path(self.output_dir, "histogram_Column1.png").exists())
        self.assertTrue(Path(self.output_dir, "histogram_Column2.png").exists())

    def test_plot_correlation_heatmap(self):
        visualizer = Visualizer(self.df, self.output_dir)
        visualizer.plot_correlation_heatmap(["Column1", "Column2"])
        self.assertTrue(Path(self.output_dir, "correlation_heatmap.png").exists())


if __name__ == "__main__":
    unittest.main()
