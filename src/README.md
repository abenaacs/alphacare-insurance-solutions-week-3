# README for `/src` Directory

## Overview

The `src` directory contains the core modules of the AlphaCare application.

## Contents

- **`app.py`:** Entry point of the application, orchestrating data loading and visualization.
- **`data_loader.py`:** Handles data ingestion and validation.
- **`visualizer.py`:** Provides functionalities for generating visualizations and statistical plots.
- **`README.md`:** Documentation for this directory.
- **`preprocessing.py`:**
  **Purpose**:
  Prepares data for analysis and modeling.
  **Key Functions**:
  load_data: Loads raw data into a pandas DataFrame.
  clean_data: Handles missing values, removes outliers, and fixes inconsistencies.
  feature_engineering: Generates new, meaningful features to improve model performance.
  encode_categorical: Converts categorical variables into a machine-learning-compatible format.

## Module Details

### `data_loader.py`

- **Purpose:** Load and validate data from various sources.
- **Key Functions:**
  - `load_data`: Reads data into a pandas DataFrame.

### `visualizer.py`

- **Purpose:** Generate visualizations based on the provided data.
- **Key Functions:**
  - `plot_histograms`: Plots histograms for numeric columns.
  - `plot_correlation_heatmap`: Generates a heatmap for correlations.
  - `plot_scatter`: Creates scatter plots for specified columns.
  - `detect_outliers`: Visualizes outliers using box plots.

### `app.py`

- **Purpose:** Main script that integrates all functionalities.
- **Key Functions:**
  - `main`: Orchestrates the application flow.
  - `visualizer.plot_*`: Calls specific visualization functions.

## Running the Application

To run the main application:

```bash
python src/app.py
```
