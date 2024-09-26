import requests
import pandas as pd


# Hämta data från Avanza url
def fetch_avanza_data():
    url = "https://www.avanza.se/_api/price-chart/stock/5247?timePeriod=three_years&resolution=day"
    response = requests.get(url)
    # Om response.status_code == 200, vilket är 'ok', returnera som pandas dataframe
    return pd.DataFrame(response.json()['ohlc']) if response.status_code == 200 else None

