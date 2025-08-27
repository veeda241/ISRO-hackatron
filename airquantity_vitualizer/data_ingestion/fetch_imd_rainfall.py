import pandas as pd

def load_imd_rainfall(path="data/raw/IMD_Rainfall.csv"):
    """Load rainfall data from IMD"""
    df = pd.read_csv(path)
    # Assuming the columns are 'date', 'city', and 'rainfall'
    # Adjust column names if they are different in the actual file
    return df[['date', 'city', 'rainfall']]
