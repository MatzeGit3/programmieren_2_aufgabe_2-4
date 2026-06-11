import json
import pandas as pd
import plotly.express as px


# Klasse EKG-Data für Peakfinder, die uns ermöglicht Peaks zu finden
class EKGdata:

    @staticmethod
    def load_by_id(ekg_id):
        """
        Instanziiert einen EKG-Test anhand der ID aus der Personen-Datenbank.
        """
        with open("data/person_db.json", "r", encoding="utf-8") as file:
            person_data = json.load(file)

        for person in person_data:
            for ekg_dict in person["ekg_tests"]:
                if ekg_dict["id"] == ekg_id:
                    return EKGdata(ekg_dict)

        return None

    # Konstruktor der Klasse soll die Daten einlesen
    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]

        self.df = pd.read_csv(
            self.data, sep="\t", header=None, names=["Messwerte in mV", "Zeit in ms"]
        )

        self.df = self.df.iloc[:5000]
        self.peaks = []

    def find_peaks(self, threshold=350):
        """
        Findet nur hohe Peaks in den EKG-Daten.
        Pro Bereich über dem threshold wird nur der höchste Punkt als Peak genommen.
        """
        peaks = []

        signal = self.df["Messwerte in mV"]

        is_above_threshold = signal > threshold

        in_peak_area = False
        peak_area_indices = []

        for index, is_above in is_above_threshold.items():

            if is_above:
                in_peak_area = True
                peak_area_indices.append(index)

            else:
                if in_peak_area:
                    peak_area = self.df.loc[peak_area_indices, "Messwerte in mV"]
                    peak_index = peak_area.idxmax()
                    peaks.append(peak_index)

                    peak_area_indices = []
                    in_peak_area = False

        if in_peak_area:
            peak_area = self.df.loc[peak_area_indices, "Messwerte in mV"]
            peak_index = peak_area.idxmax()
            peaks.append(peak_index)

        self.peaks = peaks

        self.df["is_peak"] = False
        self.df.loc[self.peaks, "is_peak"] = True

        return peaks

    def calculate_avg_hr(self):
        """
        Berechnet die durchschnittliche Herzfrequenz aus den gefundenen Peaks.
        """

        if "is_peak" not in self.df.columns:
            self.find_peaks()

        df_peaks = self.df.loc[self.df["is_peak"]]

        anzahl_peaks = len(df_peaks)

        if anzahl_peaks < 2:
            return 0

        dt_ms = df_peaks["Zeit in ms"].iloc[-1] - df_peaks["Zeit in ms"].iloc[0]
        dt_min = dt_ms / (60 * 1000)

        avg_hr = anzahl_peaks / dt_min

        return avg_hr

    def estimate_hr(self):
        """
        Berechnet die Herzfrequenz basierend auf den Peaks.
        """
        if len(self.peaks) == 0:
            self.find_peaks()

        duration_ms = self.df["Zeit in ms"].max() - self.df["Zeit in ms"].min()
        duration_min = duration_ms / 1000 / 60

        heart_rate = len(self.peaks) / duration_min

        return heart_rate

    def plot_time_series(self):
        """
        Erstellt einen Line Plot der ersten 2000 Werte
        und markiert die gefundenen Peaks.
        """
        if len(self.peaks) == 0:
            self.find_peaks()

        df_plot = self.df.head(2000).copy()

        peak_indices = [peak for peak in self.peaks if peak < 2000]
        df_peaks = self.df.loc[peak_indices]

        self.fig = px.line(
            df_plot,
            x="Zeit in ms",
            y="Messwerte in mV",
            title="EKG-Zeitreihe mit Peaks",
        )

        self.fig.add_scatter(
            x=df_peaks["Zeit in ms"],
            y=df_peaks["Messwerte in mV"],
            mode="markers",
            name="Peaks",
            marker=dict(color="red", size=8),
        )

        return self.fig


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")

    ekg = EKGdata.load_by_id(1)

    if ekg is not None:
        print(ekg.id)
        print(ekg.date)
        print(ekg.df.head())

        peaks = ekg.find_peaks()
        print("Peaks:", peaks[:10])
        print("Anzahl Peaks:", len(peaks))

        heart_rate = ekg.estimate_hr()
        print("Herzfrequenz:", heart_rate)

        avg_hr = ekg.calculate_avg_hr()
        print("Durchschnittliche Herzfrequenz:", avg_hr)

        fig = ekg.plot_time_series()
        fig.show()

    else:
        print("EKG nicht gefunden")


"""
print("This is a module with some functions to read the EKG data")
file = open("data/person_db.json")
person_data = json.load(file)
ekg_dict = person_data[0]["ekg_tests"][0]
print(ekg_dict)
ekg = EKGdata(ekg_dict)
print(ekg.df.head())
"""
