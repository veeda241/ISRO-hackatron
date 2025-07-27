# fetch_openaq_data.py
import requests
import pandas as pd

def fetch_pm25_data(city='Patna', limit=100):
    url = f"https://api.openaq.org/v2/measurements"
    params = {
        'city': city,
        'parameter': 'pm25',
        'limit': limit,
        'sort': 'desc',
        'order_by': 'datetime',
        'format': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()

    records = [
        {
            'datetime': r['date']['utc'],
            'value': r['value'],
            'unit': r['unit'],
            'location': r['location']
        } for r in data['results']
    ]
    return pd.DataFrame(records)

# Example usage
if __name__ == "__main__":
    df = fetch_pm25_data()
    df.to_csv("data/raw/pm25_patna.csv", index=False)
    print(df.head())
