

# Paket für Bearbeitung von Tabellen
import pandas as pd
import matplotlib.pyplot as plt
# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
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

def read_my_activities_csv():
    df = pd.read_csv("data/activities/activity.csv", sep=",", header=0)
    power = df["PowerOriginal"]
    return power

def make_plot_power(df):
    fig = px.line(df.head(2000), x= df.index, y="PowerOriginal")
    return fig


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

def power_max(df):
    return df.max()

def power_mean(df):
    return df.mean()

def add_Hr_Zone(df, hr_max):
    Zone_1_LOW = hr_max * 0.5
    Zone_1_HIGH = hr_max * 0.6
    Zone_2_LOW = hr_max * 0.6
    Zone_2_HIGH = hr_max * 0.7
    Zone_3_LOW = hr_max * 0.7
    Zone_3_HIGH = hr_max * 0.8
    Zone_4_LOW = hr_max * 0.8
    Zone_4_HIGH = hr_max * 0.9
    Zone_5_LOW = hr_max * 0.9
    Zone_5_HIGH = hr_max * 1.0  
    Zone_1_df = df.where((df["HeartRate"] >= Zone_1_LOW) & (df["HeartRate"] < Zone_1_HIGH))
    Zone_2_df = df.where((df["HeartRate"] >= Zone_2_LOW) & (df["HeartRate"] < Zone_2_HIGH))
    Zone_3_df = df.where((df["HeartRate"] >= Zone_3_LOW) & (df["HeartRate"] < Zone_3_HIGH))
    Zone_4_df = df.where((df["HeartRate"] >= Zone_4_LOW) & (df["HeartRate"] < Zone_4_HIGH))
    Zone_5_df = df.where((df["HeartRate"] >= Zone_5_LOW ) & (df["HeartRate"] <= Zone_5_HIGH))
    return Zone_1_df, Zone_2_df, Zone_3_df, Zone_4_df, Zone_5_df

if __name__ == "__main__":
    df = read_my_activities_csv()
    fig = make_plot_power(df)
    fig.show()    
    print(power_max(df))
    print(power_mean(df))