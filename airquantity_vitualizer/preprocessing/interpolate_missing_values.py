def interpolate_pollutants(df):
    return df.interpolate(method='linear', axis=0)
