# main.py

from src.data_collection import collect_data
from src.data_processing import process_data
from src.visualization import create_heatmap

def main():
    # Step 1: Collect Data
    print("Collecting data...")
    data = collect_data()

    # Step 2: Process Data
    print("Processing data...")
    interest_rates = process_data(data)

    # Step 3: Create Visualization
    print("Creating visualization...")
    create_heatmap(interest_rates)

if __name__ == "__main__":
    main()
