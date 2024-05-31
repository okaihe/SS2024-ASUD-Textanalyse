# Analyse von semi- und unstrukturierten Daten 🌍

Dieses Repository beinhaltet den Code, der im Rahmen der "Zusäztlichen Beteiligung" des Moduls "Analyse von semi- und unstrukturierten Daten" des Sommersemestern 2024 an der FOM erstellt wurde. Hierin enthalten sind `Jupyter-Notebooks`, die unter anderem die Generierung und Verarbeitung der Rohdaten sowie eine Sentiment-Analyse und ein Topic-Modelling der verarbeiteten Daten beinhalten.

Analysiert werden die Artikel des Nachrichtensenders N-TV.

## Inhalte 📕

Das Repository ist wie folgt aufgebaut:

- `ntv-data/` Hierin sind die Rohdaten enthalten. Die Artikel sind zunächst nach dem jeweiligen Datum und anschließend nach deren Kategorie sortiert.
- `ntv-lambda/` Hierin ist die Lambda-Funktion zum täglichen Abrufen der Artikel enthalten.
- `data.csv` Die Artikel sowie deren Überschriften und Erscheinungsdaten gesammelt in einer `csv`-Datei.
- `sentiment.csv` Die Daten der `data.csv`-Datei erweitert um die Ergebnisse der Sentiment-Analyse.
- `1-Datengenerierung.ipynb` Der Code, zum Erstellen der `data.csv`, die als Grundlage der Analyse dient.
- `2-Datenanalyse.ipynb` Die Analyse der Nachrichtenartiekl.
