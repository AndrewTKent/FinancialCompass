# src/data_collection.py

import os
import numpy as np
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

load_dotenv()

def fetch_average_mortgage_rate():
    fred_api_key = os.getenv('FRED_API_KEY')
    fred = Fred(api_key=fred_api_key)
    # Retrieve the 30-Year Fixed Rate Mortgage Average in the United States
    data = fred.get_series('MORTGAGE30US')
    # Get the latest rate
    latest_rate = data.iloc[-1]
    return latest_rate

def collect_data():
    # Fetch the base mortgage rate from FRED
    base_rate = fetch_average_mortgage_rate()

    # Define ranges for DTI and Credit Scores
    dti_range = np.arange(10, 51, 5)  # DTI from 10% to 50%
    credit_score_range = np.arange(600, 801, 20)  # Credit Scores from 600 to 800

    # Assume a loan amount in the range
    loan_amounts = [600000, 800000, 1000000, 1200000, 1500000]

    data = {
        'base_rate': base_rate,
        'dti_range': dti_range,
        'credit_score_range': credit_score_range,
        'loan_amounts': loan_amounts
    }

    return data
