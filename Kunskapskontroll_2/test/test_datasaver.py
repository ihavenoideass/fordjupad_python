import pytest
import pandas
from datasaver import DataSaver
from test_datacleaner import DataCleaner
from test_datacleaner import test_data_cleaner
from avanza_api import fetch_avanza_data



def test_data_saver():
    # Hämta och rensa data från Avanza
    data = fetch_avanza_data()

    # Skapa instans av DataCleaner
    cleaner = DataCleaner()

    # Rensa data
    cleaned_data = cleaner.clean_data(data)

    # Spara datan med DataSaver
    saver = DataSaver()
    saved_data = saver.save_data(cleaned_data)

    # Kontrollera att datan sparades korrekt
    assert not saved_data.empty
