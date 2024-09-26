#pip install yfinance

import logging
import yfinance as yf
import pandas as pd
from datetime import datetime

# Dessa variabler nedan är pekare för yfinance apiet.
ticker_symbols = 'INVE-B.ST' # Vilken/vilka aktier.
start_date = '2020-01-01' # Startdatum för kursen
end_date = datetime.now().strftime('%Y-%m-%d') # Slutdatum för kursen

class API:
    """Klass för att hämta data från apiet yfinance."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def fetch_data(self):
        """Hämtar datan från yahoo finance med hjälp av ticker_symbol, start_date och end_date."""
        # Loggar att api.py har startats, vilka tickers o tidpunkter.
        self.logger.info(f'Hämtar datan för: {ticker_symbols} från och med {start_date} till och med {end_date}.')

        try:
            # Försöker ladda ned via apiet med mina variabler.
            data = yf.download(ticker_symbols, start=start_date, end=end_date)

            # Kontrollera om datan är tom.
            if not data.empty:
                self.logger.info(f'Data har hämtats korrekt för:  {ticker_symbols}')
                return data # Retunerar data om ej tom.
            
            # Om data tom, logga nedan.
            else:
                self.logger.error(f'Datan kunde inte hämtas, {ticker_symbols}, filen är tom')
                return None
            
        except Exception as e:
            # Logga eventuella fel som inträffar under processen.
            self.logger.error(f'Ett fel uppstod vid api.py processen: {e}')
            return None





 

