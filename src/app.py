from data_loader import DataLoader
from visualizer import Visualizer
from pathlib import Path
import pandas as pd
import scipy.stats as stats
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from preprocessing import preprocess_data, encode_features
from modeling import train_linear_regression, train_random_forest
from evaluation import evaluate_model
from statistical_tests import t_test_groups


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

    # Columns definition
    categorical_columns = ["Province", "PostalCode", "Gender", "VehicleType"]
    numerical_columns = ["CarAge", "cubiccapacity", "kilowatts", "TotalPremium"]
    target_column = "TotalClaims"

    # Preprocess data
    X, y = preprocess_data(df, categorical_columns, numerical_columns, target_column)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Encode features
    X_train_combined, X_test_combined = encode_features(
        X_train, X_test, categorical_columns, numerical_columns
    )

    # PCA with fewer components
    pca = PCA(n_components=50, random_state=42)
    X_train_reduced = pca.fit_transform(X_train_combined)
    X_test_reduced = pca.transform(X_test_combined)
    # Train models
    lr_model = train_linear_regression(X_train_reduced, y_train)
    rf_model = train_random_forest(X_train_reduced, y_train)

    # Evaluate models
    evaluate_model(lr_model, X_test_reduced, y_test, "Linear Regression")
    evaluate_model(rf_model, X_test_reduced, y_test, "Random Forest")

    # Statistical tests
    province_data = df[["Province", "TotalClaims"]].dropna()
    province1 = province_data[province_data["Province"] == "Province_A"]["TotalClaims"]
    province2 = province_data[province_data["Province"] == "Province_B"]["TotalClaims"]
    t_test_groups(province1, province2, "Province TotalClaims")

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
