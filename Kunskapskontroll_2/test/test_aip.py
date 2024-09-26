import pytest
import yfinance as yf
import requests
import pandas as pd
from api import API
from avanza_api import fetch_avanza_data


# Testar om data från yfinance och Avanza API matchar
def test_compare_api_data():
    api = API()
    yf_data = api.fetch_data() # Hämta data från yfinance
    avanza_data = fetch_avanza_data() # Hämta data från Avanza

    # Jämför data
    pd.testing.assert_frame_equal(yf_data, avanza_data, check_less_precise=True)


# Error "Mixing dicts with non-Series".
# Behöver extrahera ut ohlc - pd.DataFrame(response.json()['ohlc']) för att kunna göra pandas df.
# Behöver justera så data tas från samma period, etc..
# Väljer att inte lösa detta nu men vet vad problen kan vara.
# Fortsättning följer i 'Projekt i Data Science'
