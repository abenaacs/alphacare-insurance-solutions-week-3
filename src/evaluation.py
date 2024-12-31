from sklearn.metrics import r2_score, mean_squared_error


def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluates the model and prints R² and MSE.
    """
    y_pred = model.predict(X_test)
    print(f"{model_name} R²: {r2_score(y_test, y_pred)}")
    print(f"{model_name} MSE: {mean_squared_error(y_test, y_pred)}")
