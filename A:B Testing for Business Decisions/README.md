# A/B Testing for Business Decisions

📊 Simulating A/B Tests using NumPy for data-driven business decision-making.

## 🔍 Overview
This project simulates A/B tests (e.g., for website conversion rates) to compare the performance of two variants (Group A and Group B). Using NumPy for random sampling, the script generates test data, computes conversion rates, conducts statistical hypothesis testing (t-tests), and provides recommendations based on the results. The goal is to enable data-driven decisions, such as choosing the better-performing variant for business applications.

Key features:
- Simulate binary conversion data for two groups.
- Calculate mean conversion rates.
- Perform a two-sample t-test to assess statistical significance.
- Output results and recommendations in console and CSV files.

## 🧠 Skills Used
- **NumPy**: Random data generation and numerical computations.
- **SciPy**: Statistical hypothesis testing (independent two-sample t-test).
- **Pandas**: Data manipulation and CSV file generation.
- **Statistical Analysis**: Interpreting t-test results for decision-making.
- **Data-Driven Decision Making**: Translating statistical outcomes into business recommendations.

## 📁 Files
- **`ab_testing.py`**: Main Python script containing the A/B test simulation, statistical analysis, and CSV output generation.
- **`conversion_rates.csv`**: Output CSV file with conversion rates and sample sizes for Group A and Group B.
- **`ab_test_summary.csv`**: Output CSV file with t-statistic, p-value, result, and recommendation.

## 📋 Dependencies
- Python 3.6+
- NumPy (`pip install numpy`)
- Pandas (`pip install pandas`)
- SciPy (`pip install scipy`)

Install dependencies using:
```bash
pip install numpy pandas scipy