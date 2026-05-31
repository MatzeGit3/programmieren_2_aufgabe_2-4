# Programmieren 2 – Aufgabe 2-4

Dieses Repository enthält die Abgabe zur Aufgabe **„Interaktiver Plot“** aus der Programmierübung II.

Ziel des Projekts ist es, Messdaten mit `pandas` einzulesen, aufzubereiten und anschließend in einer kleinen `Streamlit`-App interaktiv darzustellen. Die Visualisierung erfolgt mit `plotly`.

In der App werden aktuell zwei Datensätze verwendet:

1. EKG-Daten aus einer TXT-Datei
2. Aktivitätsdaten aus einer CSV-Datei

Die EKG-Daten werden im ersten Tab der App dargestellt. Die Aktivitätsdaten werden im zweiten Tab ausgewertet. Dabei werden Herzfrequenz und Leistung über die Zeit visualisiert. Zusätzlich sollen Leistungskennwerte und Herzfrequenzzonen berechnet werden.

# Ziel der Aufgabe

Die Aufgabe besteht darin, eine interaktive Streamlit-App zu erstellen, die Aktivitätsdaten auswertet.

Die App soll:

* Aktivitätsdaten aus `activity.csv` einlesen
* eine Zeitachse aus der Spalte `Duration` berechnen
* die Herzfrequenz über die Zeit darstellen
* die Leistung über die Zeit darstellen
* mittlere und maximale Leistung berechnen
* eine maximale Herzfrequenz als Eingabe erlauben
* fünf Herzfrequenzzonen berechnen
* die verbrachte Zeit pro Herzfrequenzzone anzeigen
* die durchschnittliche Leistung pro Herzfrequenzzone anzeigen

# Voraussetzungen

Um das Projekt auszuführen, werden folgende Programme benötigt:

* Python 3.14 oder passend zur Projektkonfiguration
* Git
* PDM
* optional: Visual Studio Code

Ob Python installiert ist, kann mit folgendem Befehl geprüft werden:

```bash
python -V
```

Ob PDM installiert ist, kann mit folgendem Befehl geprüft werden:

```bash
pdm --version
```

Falls PDM noch nicht installiert ist, kann es mit folgendem Befehl installiert werden:

```bash
pip install pdm
```

# Projekt klonen

Das Repository kann mit Git heruntergeladen werden:

```bash
git clone https://github.com/MatzeGit3/programmieren_2_aufgabe_2-4.git
```

Danach in den Projektordner wechseln:

```bash
cd programmieren_2_aufgabe_2-4
```

# Projekt mit PDM installieren

Das Projekt wird mit `pdm` verwaltet.

Alle benötigten Pakete stehen in der Projektkonfiguration `pyproject.toml` und werden mit folgendem Befehl installiert:

```bash
pdm install
```

Dabei wird eine virtuelle Umgebung erstellt und die benötigten Abhängigkeiten werden installiert.

Wichtig ist, dass die Datei `pdm.lock` im Repository vorhanden ist. Dadurch können andere Personen das Projekt mit denselben Paketversionen installieren.



# App starten

Die Streamlit-App kann mit folgendem Befehl gestartet werden:

```bash
pdm run streamlit run interactiv_plot.py
```

Falls die virtuelle Umgebung bereits aktiviert ist, kann die App auch direkt mit Streamlit gestartet werden:

```bash
streamlit run interactiv_plot.py
```

Nach dem Start öffnet sich die App im Browser, normalerweise unter:

```text
http://localhost:8501
```

# Aktuelle Funktionen der App

Die App kann aktuell:

* EKG-Daten einlesen
* EKG-Daten als interaktiven Plot anzeigen
* Aktivitätsdaten einlesen
* aus `Duration` eine fortlaufende Zeitachse `time_seconds` berechnen
* die Herzfrequenz über die Zeit darstellen

Zusätzlich sind beziehungsweise werden folgende Funktionen ergänzt:

* Leistung über die Zeit darstellen
* Herzfrequenz und Leistung gemeinsam plotten
* mittlere Leistung berechnen
* maximale Leistung berechnen
* maximale Herzfrequenz in der App eingeben
* fünf Herzfrequenzzonen berechnen
* Zeit pro Herzfrequenzzone anzeigen
* durchschnittliche Leistung pro Herzfrequenzzone anzeigen

# Screenshot

Die Datei `screenshot.png` zeigt einen Screenshot der Streamlit-App.

![Screenshot der Streamlit-App](data/pictures/screenshot.png)

# Ergebnis

Das Ergebnis ist eine interaktive Streamlit-App, mit der Messdaten aus CSV- und TXT-Dateien eingelesen und grafisch dargestellt werden können.

Die Aktivitätsdaten werden über eine Zeitachse visualisiert. Dadurch kann der Verlauf der Herzfrequenz und der Leistung während der Aktivität untersucht werden. Die Herzfrequenzzonen helfen zusätzlich dabei, die Belastungsintensität während der Aktivität besser einzuordnen.

