import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path
import os

# Setup paths
base_path = Path(__file__).resolve().parent.parent
csv_path = base_path / "data" / "raw" / "data.csv"
model_path = base_path / "modeling" / "AQI_model.pkl"

# Load CSV with encoding fallback
try:
    df = pd.read_csv(csv_path, encoding="utf-8")
except UnicodeDecodeError:
    print("🔄 UTF-8 failed — retrying with 'latin1'")
    df = pd.read_csv(csv_path, encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Rename standard pollution columns
df.rename(columns={
    'pm2_5': 'pm25',
    'so2': 'so2',
    'no2': 'no2',
    'rspm': 'pm10',    # use rspm or spm as proxy
    'spm': 'pm10'
}, inplace=True)

# Choose features available
features = ['pm25', 'pm10', 'no2', 'so2']
df = df[features].copy()

# Convert and drop missing values
for col in features:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.dropna(inplace=True)
print(f"✅ Cleaned rows remaining: {len(df)}")

# Create dummy AQI labels (optional)
# Here we simulate an AQI target using a synthetic formula
df['aqi'] = (
    0.5 * df['pm25'] +
    0.3 * df['pm10'] +
    0.1 * df['no2'] +
    0.1 * df['so2']
)

# Train model
X = df[features]
y = df['aqi']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Evaluate
preds = model.predict(X)
print(f"\n📊 R² Score: {r2_score(y, preds):.4f}")
print(f"📊 MSE     : {mean_squared_error(y, preds):.2f}")

# Save model
joblib.dump(model, model_path)
print(f"✅ Model saved to: {model_path}")
