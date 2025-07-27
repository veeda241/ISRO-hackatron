import pandas as pd

def load_population_stats(path="data/India_Population.csv"):
    """Load population data for scaling AQI impact"""
    df = pd.read_csv(path)
    df = df[['State', 'District', 'Population']]
    return df
