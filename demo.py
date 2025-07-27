import os
print("Current working directory:", os.getcwd())

from pathlib import Path

base_path = Path(__file__).resolve().parent.parent  # assumes you're inside /modeling/
csv_path = base_path / "data" / "raw" / "AirQualityIndia.csv"
df = pd.read_csv(csv_path)
df.replace(['-', '@'], pd.NA, inplace=True)
df.dropna(inplace=True)