from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "../data/MachineLearningRating_v3/MachineLearningRating_v3.txt"
OUTPUT_DIR = BASE_DIR / "visualizations"
SEPARATOR = "|"
NUMERIC_COLUMNS = [
    "Cylinders",
    "cubiccapacity",
    "kilowatts",
    "CustomValueEstimate",
    "SumInsured",
    "CalculatedPremiumPerTerm",
    "TotalPremium",
    "TotalClaims",
]
