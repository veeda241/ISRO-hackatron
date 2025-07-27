def merge_weather(df_aqi, df_rain):
    df = pd.merge(df_aqi, df_rain, on=['Date', 'City'], how='left')
    return df.fillna({'Rainfall_mm': 0})
