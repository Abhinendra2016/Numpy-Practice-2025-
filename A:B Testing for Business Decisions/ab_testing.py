import numpy as np
import pandas as pd
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_users = 1000
conversion_rate_a = 0.12
conversion_rate_b = 0.145

# Simulate A/B groups
group_a = np.random.binomial(1, conversion_rate_a, n_users)
group_b = np.random.binomial(1, conversion_rate_b, n_users)

# Compute stats
mean_a = np.mean(group_a)
mean_b = np.mean(group_b)
t_stat, p_value = stats.ttest_ind(group_a, group_b)
alpha = 0.05
result = "Statistically Significant" if p_value < alpha else "Not Significant"
recommendation = "Use Variant B" if p_value < alpha else "Keep Current A"

# Print results
print("Conversion Rate A: {:.2f}%".format(mean_a * 100))
print("Conversion Rate B: {:.2f}%".format(mean_b * 100))
print("T-Statistic: {:.4f}".format(t_stat))
print("P-Value: {:.4f}".format(p_value))
print("Result:", result)
print("Recommendation:", recommendation)

# Save to CSV
df = pd.DataFrame({
    "Group": ["A", "B"],
    "Conversion Rate": [mean_a, mean_b],
    "Sample Size": [n_users, n_users]
})

summary = pd.DataFrame({
    "T-Statistic": [t_stat],
    "P-Value": [p_value],
    "Result": [result],
    "Recommendation": [recommendation]
})

df.to_csv("conversion_rates.csv", index=False)
summary.to_csv("ab_test_summary.csv", index=False)

print("\n📁 CSV files saved: 'conversion_rates.csv' and 'ab_test_summary.csv'")
