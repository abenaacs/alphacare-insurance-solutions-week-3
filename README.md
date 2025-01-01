# README for AlphaCare Insurance Solutions

## Project Overview

AlphaCare Insurance Solutions is a modular, scalable, and data-driven application designed for insurance risk evaluation, customer retention prediction, and profitability analysis. Built on a foundation of Python and cutting-edge statistical modeling, this project demonstrates a comprehensive approach to solving real-world business challenges through data science and machine learning.

This application employs best practices in software development, including Object-Oriented Programming (OOP), modularity, and test-driven development, to deliver insights into key business metrics such as TotalClaims, risk differentiation, and profitability margins. Advanced tools like hypothesis testing, machine learning models, and feature interpretability methodologies further enhance the application's capabilities.

---

## Folder Structure

```
AlphaCare-Insurance-Solutions/
├── data/                      # Raw and processed data files
├── notebooks/                 # Jupyter notebooks for EDA and prototyping
│   ├── init.py
│   └── README.md
├── scripts/                   # Utility scripts for reusable functionality
│   ├── init.py
│   └── README.md
├── src/                       # Main source code for the application
│   ├── app.py                 # Application entry point
│   ├── data_loader.py         # Data ingestion and preprocessing
│   ├── visualizer.py          # Data visualization utilities
│   ├── model_builder.py       # ML model training and evaluation
│   ├── hypothesis_tester.py   # A/B testing and statistical analysis
│   └── README.md
├── tests/                     # Unit and integration tests
│   ├── test_data_loader.py
│   ├── test_visualizer.py
│   ├── test_model_builder.py
│   ├── test_hypothesis_tester.py
│   └── init.py
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files and directories to ignore
```

---

## Features

1. **Data Handling:**
   - **Flexible Data Loading:** Handles various data formats with robust validation and preprocessing.
   - **Data Segmentation:** Splits data for A/B testing and ML pipelines.

2. **Exploratory Data Analysis:**
   - Histogram plotting, correlation heatmaps, scatter plots, and box plots.

3. **Statistical Hypothesis Testing:**
   - Conducts A/B testing to identify differences in risk and profit metrics across provinces, zip codes, and demographics.
   - Uses statistical tests (t-tests, chi-squared tests) with clear interpretations.

4. **Machine Learning Modeling:**
   - Implements Linear Regression, Random Forest, and XGBoost models.
   - Evaluates models using R² and Mean Squared Error (MSE).

5. **Model Interpretability:**
   - Leverages SHAP and LIME to explain model predictions and identify key drivers.

6. **Testing and Validation:**
   - Comprehensive unit tests ensure reliability across all components.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Virtual Environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abenaacs/alphacare-insurance-solutions-week-3.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd AlphaCare-Insurance-Solutions
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # Unix-based systems
   env\Scripts\activate      # Windows
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python src/app.py
   ```

6. **Run tests:**
   ```bash
   python -m unittest discover -s tests
   ```

---

## Usage

### Hypothesis Testing
- Run `hypothesis_tester.py` to conduct A/B testing.
- Specify control (Group A) and test (Group B) datasets for experiments.
- Interpret p-values to determine statistical significance.

### Model Building and Evaluation
- Run `model_builder.py` to train predictive models.
- Choose from Linear Regression, Random Forest, or XGBoost.
- Assess performance using R² and MSE metrics.

### Model Interpretability
- Use SHAP and LIME tools within the interpretability module.
- Generate feature importance plots and analyze key drivers of predictions.

---

## Results Overview

1. **Statistical Testing Results:**
   - No significant differences in risks across provinces, zip codes, or gender (p-value ≥ 0.05).
   - Marginal insights into profitability differences.

2. **Model Performance:**
   - Linear Regression: R² = 0.014, MSE = 5,336,598
   - Random Forest: R² = -0.196, MSE = 6,474,200
   - XGBoost: R² = -0.016, MSE = 5,499,648

3. **Feature Interpretability:**
   - SHAP and LIME highlight the key drivers of predictions, enabling business decision-making.

---

## Future Enhancements

- **Data Enrichment:** Incorporate additional features to improve prediction accuracy.
- **Automated Model Tuning:** Integrate grid search or Bayesian optimization for hyperparameter tuning.
- **Expanded Hypothesis Testing:** Add more nuanced A/B testing for categorical and numerical data.
- **Enhanced Visualizations:** Include dashboards for real-time insights.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
