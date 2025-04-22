import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_csv("customer_data.csv", parse_dates=["last_purchase_date"])

# Handle future dates (force recency to be non-negative)
today = pd.Timestamp(datetime.now().date())
recency = (today - df['last_purchase_date']).dt.days.abs().values  # Fix for future dates
frequency = df['purchase_count'].values
monetary = df['total_spent'].values

# Normalization (Min-Max scaling)
scaler = MinMaxScaler()
recency_score = scaler.fit_transform(-recency.reshape(-1, 1)).flatten()  # Higher recency is bad
frequency_score = scaler.fit_transform(frequency.reshape(-1, 1)).flatten()
monetary_score = scaler.fit_transform(monetary.reshape(-1, 1)).flatten()

# Weighted RFM score (customize weights)
rfm_score = 0.5 * recency_score + 0.3 * frequency_score + 0.2 * monetary_score

# Data-driven thresholds using quartiles
quantiles = pd.qcut(rfm_score, q=3, labels=["inactive", "potential", "loyal"])
segments = df.groupby(quantiles)['customer_id'].apply(list).to_dict()

print("Customer Segments:")
print(segments)