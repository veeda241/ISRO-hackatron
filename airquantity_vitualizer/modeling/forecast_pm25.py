# forecast_pm25.py
from prophet import Prophet
import pandas as pd

df = pd.read_csv(r"D:\vyas\ISRO-hackatron\airquantity_vitualizer\data\raw\data.csv")
# Adjust the path to your CSV file as needed
# For example, it could be "data/raw/pm25_patna.csv" if you
# are using the output from fetch_openaq_data.py
# or "data/raw/pm25_data.csv" if you have a different dataset
# Adjust the path to your CSV file as needed
# For example, it could be "data/raw/pm25_patna.csv" if you
# are using the output from fetch_openaq_data.py
# or "data/raw/pm25_data.csv" if you have a different dataset

# or "data/raw/data.csv" if you have a generic dataset
# or "data/raw/data" if there's no .csv extension

  # or just "data/raw/data" if there's no .csv extension

# Ensure the CSV file has 'datetime' and 'value' columns
# If the columns are named differently, adjust accordingly
df['ds'] = pd.to_datetime(df['datetime'])
df['y'] = df['value']
df = df[['ds', 'y']]

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=24, freq='H')
forecast = model.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("models/predicted_pm25.csv", index=False)
