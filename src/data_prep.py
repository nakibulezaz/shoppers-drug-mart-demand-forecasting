import pandas as pd
import numpy as np

def load_and_merge(train_path, store_path):
    """Load train.csv and store.csv, merge them, and return a cleaned dataframe."""
    train_df = pd.read_csv(train_path)
    store_df = pd.read_csv(store_path)

    df = train_df.merge(store_df, on="Store", how="left")

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Fill missing competition distance
    df["CompetitionDistance"] = df["CompetitionDistance"].fillna(
        df["CompetitionDistance"].median()
    )

    # Feature engineering
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Quarter"] = df["Date"].dt.quarter
    df["DayOfWeek"] = df["Date"].dt.dayofweek
    df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)

    return df


def split_store_data(df, store_id, train_end_date="2014-12-31"):
    """Return train and test sets for a specific store."""
    store_df = df[df["Store"] == store_id].sort_values("Date").reset_index(drop=True)

    train = store_df[store_df["Date"] <= train_end_date]
    test = store_df[store_df["Date"] > train_end_date]

    return train, test