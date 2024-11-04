# Mortgage Interest Rate Analysis

This project analyzes how Debt-to-Income Ratio (DTI) and Credit Score affect Mortgage Interest Rates for home purchases between $600,000 and $1,500,000. It pulls data from multiple sources and visualizes the results using a heatmap.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Disclaimer](#disclaimer)

## Introduction

Understanding how DTI and Credit Score impact mortgage interest rates can help potential homebuyers make informed financial decisions. This project simulates interest rate adjustments based on these factors and visualizes the results.

## Project Structure

```
mortgage_interest_rate_analysis/
├── src/
│   ├── data_collection.py
│   ├── data_processing.py
│   └── visualization.py
├── main.py
├── README.txt
└── requirements.txt
```

- `src/`: Contains the source code modules.
- `main.py`: Main script to run the analysis.
- `README.txt`: Project documentation.
- `requirements.txt`: Python dependencies.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### 1. Clone the Repository

Create a directory for the project and place the files accordingly.

### 2. Install Required Libraries

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 3. Obtain a FRED API Key

- Sign up for a free API key from the [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/docs/api/fred/) website.
- Create a file named `.env` in the root directory.
- Add your API key to the `.env` file:

  ```
  FRED_API_KEY=your_api_key_here
  ```

### 4. Run the Project

In the terminal, execute:

```bash
python main.py
```

## Usage

The script will:

1. Collect the latest average mortgage rate from FRED.
2. Simulate interest rate adjustments based on credit scores and DTIs.
3. Generate a heatmap visualizing the estimated mortgage interest rates.

## Data Sources

- **Federal Reserve Economic Data (FRED)**: Provides the base average mortgage rate.
- **Simulated Adjustments**: Interest rate adjustments are based on typical lender practices for credit scores and DTIs.

## Disclaimer

This project is for educational purposes. The interest rates and adjustments used are illustrative and may not reflect actual lender offers or current market conditions. Always consult with a financial professional or mortgage lender for personalized advice.

---
