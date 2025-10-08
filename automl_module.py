from flaml import AutoML
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, r2_score
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# def run_automl(df: pd.DataFrame, target_col: str, task_type="auto"):
#     X = df.drop(columns=[target_col])
#     y = df[target_col]

#     # Preprocess columns
#     num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
#     cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

#     transformers = []
#     if num_cols:
#         transformers.append(("num", StandardScaler(), num_cols))
#     if cat_cols:
#         transformers.append(("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols))
#     preprocessor = ColumnTransformer(transformers)

#     # Split data
#     stratify = y if task_type=="classification" else None
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=stratify, random_state=42)

#     # Transform
#     X_train_t = preprocessor.fit_transform(X_train)
#     X_test_t = preprocessor.transform(X_test)

#     # Encode target if classification
#     if task_type=="classification":
#         le = LabelEncoder()
#         y_train = le.fit_transform(y_train)
#         y_test = le.transform(y_test)

#     # Task detection
#     if task_type=="auto":
#         task_type = "regression" if np.issubdtype(y.dtype, np.number) and y.nunique()>15 else "classification"

#     automl = AutoML()
#     metric = "accuracy" if task_type=="classification" else "r2"
#     automl.fit(X_train_t, y_train, task=task_type, metric=metric, time_budget=60)

#     # Predictions
#     y_pred = automl.predict(X_test_t)

#     # Report
#     if task_type=="classification":
#         report = classification_report(y_test, y_pred, output_dict=True)
#     else:
#         report = {"r2": r2_score(y_test, y_pred)}

#     # Save model
#     joblib.dump({"model": automl, "preprocessor": preprocessor}, "outputs/best_model.joblib")

#     return report


def run_automl(df, target_col, task):
    df = df.copy()

    # Basic validations
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in dataset.")

    # Drop rows with missing target
    df = df.dropna(subset=[target_col])
    if df.empty:
        raise ValueError("No data available after dropping rows with missing target values.")

    y = df[target_col]
    X = df.drop(columns=[target_col])

    # Encode categorical columns
    X = pd.get_dummies(X, drop_first=True)

    # Handle target encoding
    if y.dtype == 'object' or y.dtype.name == 'category':
        le = LabelEncoder()
        y = le.fit_transform(y)
        if task == "regression":
            task = "classification"  # Switch to classification if categorical target detected

    # Ensure there’s variation in target
    if len(np.unique(y)) < 2:
        raise ValueError("Target column has only one unique value — cannot train model.")

    # Split data
    le = LabelEncoder()
    y = le.fit_transform(y) 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y if task=="classification" else None)

    automl = AutoML()
    settings = {
        "time_budget": 60,  # seconds
        "metric": "r2" if task == "regression" else "accuracy",
        "task": task,
        "log_file_name": "automl.log",
    }

    # Train model safely
    try:
        automl.fit(X_train=X_train, y_train=y_train, **settings)
    except Exception as e:
        error_msg = str(e)
        if "special JSON characters" in error_msg:
            st.error(
                "⚠️ AutoML training failed due to unsupported special characters in column names. "
                "Please check your dataset column names for unusual symbols or invisible characters, "
                "clean them, and re-upload the dataset."
            )
        else:
            st.error(f"❌ AutoML training failed: {error_msg}")

    # Evaluate
    y_pred = automl.predict(X_test)
    score = automl.score(X_test, y_test)

    # Report
    result = {
        "best_model": str(automl.model),
        "best_estimator": automl.best_estimator,
        "metric": settings["metric"],
        "score": float(score),
        "time_taken_sec": automl.best_config_per_estimator.get(automl.best_estimator, {}).get("train_time", "N/A"),
    }

    return result