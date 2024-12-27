# README for Project Root

## Project Overview

AlphaCare Insurance Solutions is a modular and scalable data visualization and analysis application. The project demonstrates a well-structured Python application adhering to best practices in Object-Oriented Programming (OOP), data handling, and visualization.

## Folder Structure

```
AlphaCare-Insurance-Solutions/
├── data/
├── notebooks/
│   ├── init.py
│   └── README.md
├── scripts/
│   ├── init.py
│   └── README.md
├── src/
│   ├── app.py
│   ├── data_loader.py
│   ├── visualizer.py
│   └── README.md
├── tests/
│   ├── test_data_loader.py
│   ├── test_visualizer.py
│   └── init.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

1. **Data Loading:** Flexible data loading with validation.
2. **Visualization:** Histogram plotting, correlation heatmaps, scatter plots, and box plots.
3. **Modular Design:** Clear separation of concerns with reusable modules.
4. **Testing:** Comprehensive unit tests to ensure functionality.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/abenaacs/alphacare-insurance-solutions-week-3.git
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate # For Unix-based systems
   env\Scripts\activate   # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python src/app.py
   ```
5. Run tests:
   ```bash
   python -m unittest discover -s tests
   ```
