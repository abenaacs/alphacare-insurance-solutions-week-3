from data_loader import DataLoader
from visualizer import Visualizer
from pathlib import Path


def main():
    # Define paths using Path module
    current_dir = Path(__file__).parent
    data_path = (
        current_dir / "../data/MachineLearningRating_v3/MachineLearningRating_v3.txt"
    )
    output_dir = current_dir / "visualizations"

    # Convert data_path to an absolute path
    data_path = data_path.resolve()

    # Check if the file exists
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found at: {data_path}")

    # Load data
    loader = DataLoader(data_path)
    df = loader.load_data()
    loader.summarize_data()

    # Visualize data
    visualizer = Visualizer(df, output_dir)
    numeric_columns = [
        "Cylinders",
        "cubiccapacity",
        "kilowatts",
        "CustomValueEstimate",
        "SumInsured",
        "CalculatedPremiumPerTerm",
        "TotalPremium",
        "TotalClaims",
    ]
    visualizer.plot_histograms(numeric_columns)
    visualizer.plot_correlation_heatmap(numeric_columns)


if __name__ == "__main__":
    main()
