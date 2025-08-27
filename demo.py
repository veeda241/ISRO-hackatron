import os
print("Current working directory:", os.getcwd())

from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent
csv_path = base_path / "airquantity_vitualizer" / "data" / "raw" / "data.csv"
print(f"Loading data from: {csv_path}")
df = pd.read_csv(csv_path)
df.replace(['-', '@'], pd.NA, inplace=True)
df.dropna(inplace=True)
print("Data loaded and cleaned successfully.")
