import pandas as pd 
import plotly.express as px

def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

def read_my_activity():
    df = pd.read_csv("data/activities/activity.csv")
    df["time_seconds"] = df["Duration"].cumsum()
    return df
   # df["time_seconds"]



def make_power_hr_plot(df):
    fig = px.line(
        df,
        x="time_seconds",
        y="HeartRate",
        title="Herzfrequenz über Zeit",
        labels={
            "time_seconds": "Zeit [s]",
            "HeartRate": "Herzfrequenz [bpm]"
        }
    )
    return fig
   
    
def add_hr_zones(df, hr_max):
    bins = [0, hr_max * 0.6, hr_max * 0.7, hr_max * 0.8, hr_max * 0.9, hr_max]
    labels = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"]

    df["HR Zone"] = pd.cut(
        df["HeartRate"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

if __name__ == "__main__":
    df = read_my_activity()
    fig = make_power_hr_plot(df)
    fig.show()