# forecast_pm25.py
from prophet import Prophet
import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
csv_path = base_path / "data" / "raw" / "data.csv"
df = pd.read_csv(csv_path)


# Ensure the CSV file has 'datetime' and 'value' columns
# If the columns are named differently, adjust accordingly
df['ds'] = pd.to_datetime(df['datetime'])
df['y'] = df['value']
df = df[['ds', 'y']]

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=24, freq='H')
forecast = model.predict(future)
output_path = base_path / "modeling" / "predicted_pm25.csv"
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(output_path, index=False)
print(f"Forecast saved to: {output_path}")
