
# Data Pipeline Project
Detta projekt är utformat för att hämta aktiekursdata från yahoo finance, rengöra datan och spara den för framtida analys. Projektet inkluderar även testning med pytest för att säkerställa funktionalitet.
Vid testningen användes ett annat api från Avanza för att säkerställa om pipeline-stegen fungerar korrekt för annan api utöver yahoo

## Paket att installera
```shell
pip install yfinance
pip install requests


```

## Hur använder man orginal API:et?

Se länk nedan vilka metoder och liknande som finns att tillgå.

```shell
https://aroussi.com/post/python-yahoo-finance


```

## Hämtning av data via min api klass (Yahoo)

```shell

from api import API
api = API()
data = api.fetch_data()

```

## Hämtning av data via min api klass (Avanza)

```shell

from avanza_api import fetch_avanza_data
avanza_data = fetch_avanza_data()

```

## Rengörning av data

```shell

from datacleaner import DataCleaner
cleaner = DataCleaner()
cleaned_data = cleaner.clean_data(data)

```

## Nedsparning av data

```shell

from datasaver import DataSaver
saver = DataSaver()
saver.save_data(cleaned_data)

```