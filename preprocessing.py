import pandas as pd
import numpy as np
import re
import unicodedata

def clean_column_names(df):
    clean_cols = []
    for col in df.columns:
        # Convert to string
        col_str = str(col)
        # Normalize Unicode
        col_str = unicodedata.normalize("NFKD", col_str)
        # Remove all control characters (non-printable)
        col_str = "".join(ch for ch in col_str if unicodedata.category(ch)[0] != "C")
        # Replace any non-alphanumeric character with underscore
        col_str = re.sub(r'[^\w]', '_', col_str)
        # Lowercase
        col_str = col_str.lower()
        # Ensure name does not start with digit
        if re.match(r'^\d', col_str):
            col_str = f"_{col_str}"
        clean_cols.append(col_str)
    df.columns = clean_cols
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    
    df_clean = clean_column_names(df_clean)

    # Fill missing numeric values
    num_cols = df_clean.select_dtypes(include=[np.number]).columns
    df_clean[num_cols] = df_clean[num_cols].fillna(0)

    # Fill missing categorical values
    cat_cols = df_clean.select_dtypes(include=["object", "category", "bool"]).columns
    df_clean[cat_cols] = df_clean[cat_cols].fillna("Unknown")

    # Optional: group rare categories
    for col in cat_cols:
        counts = df_clean[col].value_counts()
        rare = counts[counts < 2].index
        df_clean[col] = df_clean[col].replace(rare, "Other")

    

    return df_clean
