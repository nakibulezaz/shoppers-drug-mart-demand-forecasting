# Demand Forecasting and Strategic Analysis for Shoppers Drug Mart

This project analyzes 1,017,209 daily sales records across 1,115 stores (2013–2015) to identify the key drivers of retail performance and build accurate demand forecasting models. The analysis includes exploratory data analysis (EDA), promotional uplift measurement, PCA, SARIMA and Prophet forecasting, and business recommendations.

---

## Project Overview

Key insights from the analysis:

- Promotions increase sales by **81.4%**, making them the strongest driver of revenue.
- Store location has **near-zero impact** on sales (correlation = -0.019).
- Store Type B outperforms other formats by **approximately 77%**.
- Prophet provides more accurate forecasts than SARIMA for early‑year sales.

The project includes full code, notebooks, visualizations, and a technical report.

---

## Repository Structure

```
shoppers-drug-mart-demand-forecasting/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda_promo_location_storetype.ipynb
│   ├── 02_pca_competition.ipynb
│   └── 03_sarima_prophet_forecasting.ipynb
│
├── src/
│   ├── data_prep.py
│   ├── eda.py
│   ├── modeling_sarima.py
│   └── modeling_prophet.py
│
├── reports/
│   ├── shoppers_demand_forecasting_report.pdf
│   └── figures/
│       ├── seasonality_heatmap.png
│       ├── promo_uplift.png
│       ├── competition_distance.png
│       ├── store_type_performance.png
│       └── model_comparison.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dataset Summary

| Metric | Value |
|--------|-------|
| Total Records | 1,017,209 |
| Number of Stores | 1,115 |
| Date Range | 2013-01-01 to 2015-12-31 |
| Key Variables | Sales, Promo, StoreType, CompetitionDistance, Holidays |

Note: Dataset is publicly available (e.g., Rossmann/Shoppers dataset). Place CSV files inside `data/raw/`.

---

## Exploratory Data Analysis (EDA)

### Seasonal Patterns

- December shows the highest sales across all years (about 40 percent above annual average).
- August and September show a seasonal dip (about 13 percent below average).
- Seasonal patterns are stable and predictable.

Figure: `reports/figures/seasonality_heatmap.png`

---

### Promotional Impact

Promotions are the strongest driver of sales.

| Metric | No Promo | With Promo | Uplift |
|--------|----------|------------|--------|
| Average Daily Sales | 4406 | 7991 | +81.4% |

Figure: `reports/figures/promo_uplift.png`

---

### Location and Competition

- Correlation between CompetitionDistance and Sales: -0.019
- No meaningful trend in scatter plot
- Location-based strategies do not improve sales

Figure: `reports/figures/competition_distance.png`

---

### Store Format Performance

| Store Type | Average Sales | Percent vs Type A |
|------------|---------------|-------------------|
| A | 5738 | Baseline |
| B | 10058 | +77% |
| C | 5724 | -0.2% |
| D | 5642 | -1.7% |

Figure: `reports/figures/store_type_performance.png`

---

## PCA: Competitive Environment Analysis

Features analyzed:

- CompetitionDistance  
- Promo2SinceYear  
- CompetitionOpenSinceYear  

Findings:

- All three components are required to retain 90 percent variance.
- Competitive environment is multi-dimensional.
- These features still do not meaningfully predict sales.

---

## Time Series Forecasting

Models developed:

- SARIMA (weekly seasonality)
- Prophet (yearly and weekly seasonality with holidays)

Prophet achieves lower MAPE and captures holiday effects more effectively.

Figure: `reports/figures/model_comparison.png`

---

## Strategic Recommendations

1. Prioritize promotions  
   - Allocate 60 to 70 percent of marketing budget to promotions  
   - Run weekly promotional cycles  
   - Test promotion types (percentage discounts, bundles, BOGO)

2. Expand Store Type B format  
   - Type B stores generate 77 percent more revenue  
   - Upgrade or replace Type A, C, and D stores where feasible

3. Do not invest in location-based strategies  
   - Location has no measurable impact on sales  
   - Focus on store format, assortment, and promotions

4. Use forecasting models for inventory planning  
   - Increase inventory before November and December  
   - Use Prophet forecasts for early-year planning

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/shoppers-drug-mart-demand-forecasting.git
cd shoppers-drug-mart-demand-forecasting
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook

```
jupyter notebook
```

Open the notebooks in the following order:

1. 01_eda_promo_location_storetype.ipynb  
2. 02_pca_competition.ipynb  
3. 03_sarima_prophet_forecasting.ipynb  

---

## Full Technical Report

The complete analysis, visuals, and business recommendations are available here:

`reports/shoppers_demand_forecasting_report.pdf`

---

## Author

Mohammad Nakibul Ezaz  
MSc Artificial Intelligence and Data Science  
University of Hull
