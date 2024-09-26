import pytest
import pandas as pd
from datacleaner import DataCleaner
from avanza_api import fetch_avanza_data

def test_data_cleaner():
    # Hämta data från Avanza
    data = fetch_avanza_data()

    # Skapa instans av DataCleaner
    cleaner = DataCleaner()

    # Rensa data
    cleaned_data = cleaner.clean_data(data)

    # Kontrollera om kolumnerna har tagits bort korrekt
    assert 'Open' not in cleaned_data.columns
    assert 'High' not in cleaned_data.columns
    assert 'Low' not in cleaned_data.columns
    assert 'Adj Close' not in cleaned_data.columns