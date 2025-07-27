import pandas as pd

def load_cpcb_dataset(path="data/CPCB_AQI.csv"):
    """Load AQI data from CPCB source"""
    df = pd.read_csv(path)
    df.replace(["-", "@", "NA"], pd.NA, inplace=True)
    return df.dropna()
