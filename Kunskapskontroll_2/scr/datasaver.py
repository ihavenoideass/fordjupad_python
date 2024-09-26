import logging

class DataSaver:
    """Klass för att spara datan till en csv fil."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def save_data(self, data):
        """Sparar ned data till .csv"""
        self.logger.info('Sparar data till .cvs')

        try:
            # Försöker spara ned datafilen till csv
            data.to_csv('aktier.csv', index=True)

            if not data.empty:
                self.logger.info('Datan har sparats korrekt.')
                return data  # Returnera data för sparande.
            
            # Om data tom, logga nedan
            else:
                self.logger.error('Datan kunde inte sparas, filen är tom.')
                return None

        except Exception as e:
            # Logga eventuella fel som inträffar under processen.
            self.logger.error(f'Ett fel uppstod vid datasaver.py processen: {e}')
            return None