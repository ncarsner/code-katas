# import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import random


# Sales and Advertising Spend
data = {
    "Advertising_Spend": [random.randint(1, 10) * 50 for _ in range(5)],
    "Sales": [random.randint(1, 10) * 10 for _ in range(5)],  # Linear relationship
    "Customer_Satisfaction": [random.randint(1, 5) for _ in range(5)],  # Non-linear relationship
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Pearson and Spearman coefficients
pearson_sales_ad = pearsonr(df["Advertising_Spend"], df["Sales"])[0]
spearman_sales_ad = spearmanr(df["Advertising_Spend"], df["Sales"])[0]

pearson_satisfaction_ad = pearsonr(df["Advertising_Spend"], df["Customer_Satisfaction"])[0]
spearman_satisfaction_ad = spearmanr(df["Advertising_Spend"], df["Customer_Satisfaction"])[0]

print(f"Spend: {data['Advertising_Spend']}")
print(f"Sales: {data['Sales']}")
print(f"Satisfaction: {data['Customer_Satisfaction']}")

print("\nCorrelation - Advertising Spend :: Sales:")
print(f"Pearson: {pearson_sales_ad:.2f}")
print(f"Spearman: {spearman_sales_ad:.2f}")

print("\nCorrelation - Advertising Spend :: Customer Satisfaction:")
print(f"Pearson: {pearson_satisfaction_ad:.2f}")
print(f"Spearman: {spearman_satisfaction_ad:.2f}")
