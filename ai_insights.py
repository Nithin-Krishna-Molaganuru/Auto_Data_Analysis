import streamlit as st
import os
import requests
import pandas as pd
import numpy as np

API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_TOKEN = st.secrets.get("Auto_DA")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}  # Make sure HF_TOKEN is set in environment

def generate_ai_insights(df: pd.DataFrame, target_col: str, task_type: str):
    st.subheader(
        "The AI may crash with very long prompts or large datasets. "
        "If it doesn't respond, try again with a smaller dataset or summary. "
        "For very large inputs, consider adjusting using AutoEDA and AutoML features."
    )

    if "HF_TOKEN" == None:
        raise ValueError("HF_TOKEN is Null. Please add it to run AI insights.")

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_numeric = df[numeric_cols]

    missing_values = df.isna().sum()
    correlations = df_numeric.corr()
    outliers = ((df_numeric < df_numeric.quantile(0.05)) | (df_numeric > df_numeric.quantile(0.95))).sum()
    summary_stats = df_numeric.describe().T


    # Build a compact dataset summary
    summary = f"""
    Dataset Summary:
    - Rows: {df.shape[0]}
    - Columns: {df.shape[1]}
    - Missing Values: {missing_values.to_dict()}
    - Numeric Summary: {summary_stats.head(5).to_dict()}
    - Feature Correlations: {correlations.to_dict()}
    - Potential Outliers (count per column): {outliers.to_dict()}

    Target: {target_col}
    Task: {task_type}
    """

    messages = [
        {"role": "system", "content": "You are an expert AI data analyst."},
        {"role": "user", "content": f"Analyze the dataset using the above summary : {summary} and give actionable insights. Include interpretation for each statistic and feature."}
    ]

    payload = {
        "model": "Qwen/Qwen2.5-7B:featherless-ai",  # Replace with your desired chat model
        "messages": messages,
        "temperature": 0.0
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=180)

    if response.status_code != 200:
        return f"HF API error: {response.status_code} {response.text}"

    data = response.json()

    # Extract assistant's reply
    try:
        reply = data["choices"][0]["message"]["content"]
        return reply
    except (KeyError, IndexError):
        return str(data)

# Example usage
# response_text = generate_ai_insights(df, "target_column_name", "regression")
# print(response_text)

