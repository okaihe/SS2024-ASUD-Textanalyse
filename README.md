# Analyse von semi- und unstrukturierten Daten 🌍

Dieses Repository beinhaltet den Code, der im Rahmen der "Zusäztlichen Beteiligung" des Moduls "Analyse von semi- und unstrukturierten Daten" des Sommersemestern 2024 an der FOM erstellt wurde. Hierin enthalten sind `Jupyter-Notebooks`, die unter anderem die Generierung und Verarbeitung der Rohdaten sowie eine Sentiment-Analyse und ein Topic Modeling der verarbeiteten Daten beinhalten.

Analysiert werden die Artikel des Nachrichtensenders N-TV.

## Inhalte 📕

Das Repository ist wie folgt aufgebaut:

- `ntv-data/` Hierin sind die Rohdaten enthalten. Die Artikel sind zunächst nach dem jeweiligen Datum und anschließend nach deren Kategorie sortiert.
- `ntv-lambda/` Hierin ist die Lambda-Funktion zum täglichen Abrufen der Artikel enthalten.
- `1-1-Datengenerierung.ipynb` Der Code, zum Erstellen der Datei `2-1-data.csv`, die als Grundlage der Analyse dient und die Daten zu den Artikeln beinhaltet.
- `1-2-Datenanalyse.ipynb` Enhält den Code zur Sentiment-Analyse und dem Topic Modeling.
- `2-1-data.csv` Die Artikel sowie deren Überschriften und Erscheinungsdaten gesammelt in einer `csv`-Datei.
- `2-2-sentiment.csv` Die Daten der `data.csv`-Datei erweitert um die Ergebnisse der Sentiment-Analyse.
- `2-3-topics.csv` Die Ergebnisse des Topic Modelings.
