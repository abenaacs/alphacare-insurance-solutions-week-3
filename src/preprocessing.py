import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import csr_matrix, hstack


def preprocess_data(df, categorical_columns, numerical_columns, target_column):
    """
    Cleans and preprocesses the dataset for modeling.
    """

    # Feature engineering
    if "RegistrationYear" in df.columns:
        df["CarAge"] = 2024 - df["RegistrationYear"]
    # Handle missing values
    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    df[categorical_columns] = df[categorical_columns].fillna("Unknown")
    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())

    # Splitting features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def encode_features(X_train, X_test, categorical_columns, numerical_columns):
    """
    Encodes categorical features and combines them with numerical features.
    """
    encoder = OneHotEncoder(sparse_output=True, handle_unknown="ignore")
    encoded_train = encoder.fit_transform(X_train[categorical_columns])
    encoded_test = encoder.transform(X_test[categorical_columns])

    # Convert numerical features to sparse format
    X_train_numerical_sparse = csr_matrix(X_train[numerical_columns].values)
    X_test_numerical_sparse = csr_matrix(X_test[numerical_columns].values)

    # Combine categorical and numerical features
    X_train_combined = hstack((X_train_numerical_sparse, encoded_train))
    X_test_combined = hstack((X_test_numerical_sparse, encoded_test))

    return X_train_combined, X_test_combined
