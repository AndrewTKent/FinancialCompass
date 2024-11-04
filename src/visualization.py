# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def create_heatmap(interest_rates):
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        interest_rates,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd",
        cbar_kws={'label': 'Interest Rate (%)'},
        linewidths=0.5,
        linecolor='gray'
    )
    plt.title('Estimated Mortgage Interest Rates\nLoan Amount: $1,000,000', fontsize=16)
    plt.xlabel('Debt-to-Income Ratio (%)', fontsize=14)
    plt.ylabel('Credit Score', fontsize=14)
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()
