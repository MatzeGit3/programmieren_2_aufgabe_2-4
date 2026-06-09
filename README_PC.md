# Leistungskurve II

Dieses Projekt berechnet eine Power Curve aus Leistungsdaten eines Radfahrers. Die Power Curve zeigt für verschiedene Zeitfenster die jeweils höchste durchschnittliche Leistung.

## Funktionen

* Einlesen der Aktivitätsdaten aus einer CSV-Datei
* Berechnung der besten Durchschnittsleistung für verschiedene Zeitfenster
* Erstellung eines DataFrames mit den Ergebnissen
* Visualisierung der Power Curve mit Plotly
* Darstellung der Ergebnisse in einer Streamlit-Anwendung

## Verwendete Technologien

* Python
* Pandas
* Plotly
* Streamlit

## Projektstruktur

```text
.
├── data/
│   └── activities/
│       └── activity.csv
├── src/
│   ├── functions.py
│   └── interactive_plot.py
├── screenshot.png
├── pyproject.toml
└── README.md
```

## Installation

Abhängigkeiten installieren:

```bash
pdm install
```

## Anwendung starten

Die Streamlit-Anwendung kann mit folgendem Befehl gestartet werden:

```bash
pdm run streamlit run src/interactive_plot.py
```

Alternativ:

```bash
streamlit run src/interactive_plot.py
```

## Ausgabe

Die Anwendung erzeugt:

* eine Tabelle mit den berechneten Leistungswerten
* eine grafische Darstellung der Power Curve

Die x-Achse zeigt die Zeitfenster (z.B. 10 s, 30 s, 1 min, 5 min, 30 min), die y-Achse die jeweils höchste durchschnittliche Leistung in Watt.

## Screenshot

Ein Screenshot der Anwendung befindet sich in der Datei:

```text
screenshot.png
```

```
```
