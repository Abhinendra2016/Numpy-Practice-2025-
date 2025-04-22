# 🎯 Customer Segmentation Engine: RFM Analysis with Behavioral Insights

**Leverage advanced RFM (Recency-Frequency-Monetary) modeling to identify customer value segments using Python's scientific stack.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

## 🌟 Key Features
- Temporal-aware customer value scoring
- Dynamic segmentation using quantile-based thresholds
- Robust normalization for outlier-resistant scoring
- Configurable metric weights for business prioritization
- Future-date handling for real-world data robustness

## 📊 Optimized RFM Methodology

| Metric      | Calculation                          | Business Insight                   |
|-------------|--------------------------------------|-------------------------------------|
| **Recency** | Days since last purchase             | Customer engagement recency        |
| **Frequency**| Total transactions count            | Purchasing habit consistency       |
| **Monetary** | Total lifetime spending             | Customer economic value            |

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy pandas scikit-learn

## 🛠️ How It Works

- Load customer data
- Calculate RFM values using NumPy
- Segment customers into:
  - **Loyal**
  - **Potential**
  - **Inactive**

## 📁 Files

- `customer_segmentation_rfm.py`: Core logic using NumPy
- `customer_data.csv`: Sample customer purchase data
- `.gitignore`: Python cache and environment exclusion

## ▶️ Run the Project

```bash
python customer_segmentation_rfm.py
