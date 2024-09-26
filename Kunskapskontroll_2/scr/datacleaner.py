import logging
import pandas as pd 

# Listar upp kolumnerna jag vill ta bort.
COLUMNS_TO_DROP = ["Adj Close", "High", "Low", "Open"]

class DataCleaner:
    """Klass för att städa data, tar bort kolumner."""
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def clean_data(self, data):
        """Rengör data hämtad från API, tar bort kolumner."""
        # Logga att datacleaner har startats.
        self.logger.info('Startar datarensning från api.fetch_data')
       
        try:
            # Försöker ta bort de kolumner som finns i COLUMNS_TO_DROP och rundar av till två decimaler.
            data_cleaned = round(data.drop(columns=COLUMNS_TO_DROP, axis=1), 2)
            
            # Kontrollera om datan är tom.
            if not data_cleaned.empty:
                self.logger.info('Datan har rensats och transformerats korrekt.')
                return data_cleaned  # Returnera rensad data.
            
            # Om data tom, logga nedan
            else:
                self.logger.error('Datan kunde inte rensas, filen är tom efter transformering.')
                return None

        except Exception as e:
            # Logga eventuella fel som inträffar under processen.
            self.logger.error(f'Ett fel uppstod vid datacleaner.py processen: {e}')
            return None
            




