import pandas as pd

def load_openaq_file(path="data/OpenAQ_PM25.csv"):
    """Load PM2.5 readings from OpenAQ"""
    df = pd.read_csv(path)
    df = df[df['parameter'] == 'pm25']
    return df[['city', 'value', 'date.local']]
