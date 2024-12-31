from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def train_linear_regression(X_train, y_train):
    """
    Trains a linear regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train, n_estimators=100):
    """
    Trains a random forest regressor.
    """
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    return model
