import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def scale_numeric(df, numeric_cols):
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df, scaler

def encode_labels(df, col):
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    return df, le

def clean_text(df, col):
    import re
    df[col] = df[col].astype(str).str.lower()
    df[col] = df[col].apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x))
    return df
