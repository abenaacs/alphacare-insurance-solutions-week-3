import shap


def explain_model_with_shap(model, X_train, X_test, feature_names):
    """
    Explains the Random Forest model using SHAP.
    """
    explainer = shap.Explainer(
        model, X_train, check_additivity=False
    )  # Disable additivity check for complex cases
    shap_values = explainer(X_test)

    # Visualize SHAP results
    shap.summary_plot(shap_values, features=X_test, feature_names=feature_names)
