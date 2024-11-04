# src/data_processing.py

import numpy as np
import pandas as pd

def loan_amount_adjustment(loan_amount):
    # Jumbo loan limit as of 2023 is $726,200
    if loan_amount > 726200:
        return 0.25  # Add 0.25% for jumbo loans
    else:
        return 0

def process_data(data):
    base_rate = data['base_rate']
    dti_range = data['dti_range']
    credit_score_range = data['credit_score_range']
    loan_amounts = data['loan_amounts']

    # We'll focus on a single loan amount for simplicity
    loan_amount = 1000000  # $1,000,000

    # Create a DataFrame to store interest rates
    interest_rates = pd.DataFrame(index=credit_score_range, columns=dti_range)

    for credit_score in credit_score_range:
        for dti in dti_range:
            rate = base_rate

            # Adjust rate based on credit score
            if credit_score >= 760:
                credit_adjustment = 0  # Best rates
            elif credit_score >= 740:
                credit_adjustment = 0.125
            elif credit_score >= 720:
                credit_adjustment = 0.25
            elif credit_score >= 700:
                credit_adjustment = 0.375
            elif credit_score >= 680:
                credit_adjustment = 0.5
            elif credit_score >= 660:
                credit_adjustment = 0.625
            elif credit_score >= 640:
                credit_adjustment = 0.75
            elif credit_score >= 620:
                credit_adjustment = 0.875
            else:
                credit_adjustment = 1.0  # Higher risk

            rate += credit_adjustment

            # Adjust rate based on DTI
            if dti > 43:
                dti_adjustment = 0.5
            elif dti > 36:
                dti_adjustment = 0.25
            else:
                dti_adjustment = 0

            rate += dti_adjustment

            # Adjust rate based on loan amount (jumbo loan)
            rate += loan_amount_adjustment(loan_amount)

            # Store the calculated rate
            interest_rates.at[credit_score, dti] = rate

    # Convert DataFrame values to float
    interest_rates = interest_rates.astype(float)

    return interest_rates
