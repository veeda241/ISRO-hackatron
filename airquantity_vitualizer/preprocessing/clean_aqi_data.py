def clean_aqi(df):
    df.replace(['-', '@'], pd.NA, inplace=True)
    df.dropna(subset=['PM2.5', 'PM10', 'NO2', 'SO2'], inplace=True)
    df[['PM2.5', 'PM10', 'NO2', 'SO2']] = df[['PM2.5', 'PM10', 'NO2', 'SO2']].astype(float)
    return df
