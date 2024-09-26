import logging
from api import API
from datacleaner import DataCleaner
from datasaver import DataSaver
import sqlite3
import pandas as pd

logger = logging.getLogger(__name__)
# Loggning 
logging.basicConfig(
    filename='logger.log', 
    format='[%(asctime)s][%(name)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.INFO)



api = API()
dc = DataCleaner()
ds = DataSaver()

logger.info('Startar data pipelinen...')

# Kör pipelinen
data = api.fetch_data()
cleaned_data = dc.clean_data(data)
ds.save_data(cleaned_data)

# Skapar en connection och en sql-databas.
con = sqlite3.connect('aktie.db')
cleaned_data.to_sql('aktiekurs', con, if_exists='replace')