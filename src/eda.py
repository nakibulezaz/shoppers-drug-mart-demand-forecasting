import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_style("darkgrid")


def plot_seasonality(df):
    pivot = df.groupby(["Year", "Month"])["Sales"].mean().reset_index()
    heatmap_data = pivot.pivot(index="Year", columns="Month", values="Sales")

    plt.figure(figsize=(12, 5))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlOrRd")
    plt.title("Monthly Sales Seasonality Across Years")
    plt.show()


def promo_uplift(df):
    promo_yes = df[df["Promo"] == 1]["Sales"]
    promo_no = df[df["Promo"] == 0]["Sales"]

    uplift = (promo_yes.mean() - promo_no.mean()) / promo_no.mean() * 100
    print(f"Promotional uplift: {uplift:.2f}%")

    plt.figure(figsize=(12, 5))
    sns.kdeplot(promo_no, label="No Promo")
    sns.kdeplot(promo_yes, label="Promo")
    plt.title("Sales Distribution by Promotion Status")
    plt.legend()
    plt.show()


def competition_scatter(df):
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x="CompetitionDistance", y="Sales", data=df, alpha=0.2)
    plt.title("Sales vs Competition Distance")
    plt.show()


def store_type_performance(df):
    plt.figure(figsize=(10, 5))
    sns.boxplot(x="StoreType", y="Sales", data=df)
    plt.title("Sales Distribution by Store Type")
    plt.show()