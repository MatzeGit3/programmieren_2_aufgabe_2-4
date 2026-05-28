


import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px







def read_my_activities_csv():
    df = pd.read_csv("data/activities/activity.csv", sep=",", header=0)
    return df

def make_plot_power(df):
    fig = px.line(df, x= df.index, y="PowerOriginal")
    return fig


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df, x= "Zeit in ms", y="Messwerte in mV")
    return fig

def power_max(df):
    return df.max()

def power_mean(df):
    return df.mean()

def make_hr_plot(df):
    fig = px.line(df, x= df.index, y="HeartRate")
    return fig

def make_power_and_hr_plot(df, max_heart_rate, zones):
    plot_df = df[["PowerOriginal", "HeartRate"]].copy()

    plot_df["Index"] = df.index

    plot_df = plot_df.melt(
        id_vars="Index",
        value_vars=["PowerOriginal", "HeartRate"],
        var_name="Messgröße",
        value_name="Wert"
    )

    fig = px.line(
        plot_df,
        x="Index",
        y="Wert",
        color="Messgröße",
        title="Power und Herzfrequenz"
    )

    # HeartRate-Kurve auf die rechte y-Achse legen
    for trace in fig.data:
        if trace.name == "HeartRate":
            trace.yaxis = "y2"

    # zweite y-Achse rechts erstellen
    fig.update_layout(
        xaxis_title="Zeit",
        yaxis=dict(
            title="Power [W]"
        ),
        yaxis2=dict(
            title="Herzfrequenz [bpm]",
            overlaying="y",
            side="right"
        )
    )

    # Herzfrequenzzonen auf rechter y-Achse einzeichnen
    for zone_name, (lower_percent, upper_percent, color) in zones.items():
        lower_bpm = max_heart_rate * lower_percent
        upper_bpm = max_heart_rate * upper_percent

        fig.add_hrect(
            y0=lower_bpm,
            y1=upper_bpm,
            opacity=0.18,
            line_width=0,
            fillcolor=color,
            annotation_text=zone_name,
            annotation_position="right",
            yref="y2"
        )

    return fig
def zones():
    zones = {
        "Zone 1": (0.50, 0.60, "lightblue"),
        "Zone 2": (0.60, 0.70, "lightgreen"),
        "Zone 3": (0.70, 0.80, "yellow"),
        "Zone 4": (0.80, 0.90, "orange"),
        "Zone 5": (0.90, 1.00, "red")
    }

    return zones

def time_in_heart_rate_zones(df, max_heart_rate, zones):
    df = df.copy()

    # Falls jede Zeile 1 Sekunde entspricht
    df["Zeitdifferenz in s"] = 1

    

    results = []

    for zone_name, (lower_percent, upper_percent, color) in zones.items():
        lower_bpm = max_heart_rate * lower_percent
        upper_bpm = max_heart_rate * upper_percent

        time_in_zone_s = df[
            (df["HeartRate"] >= lower_bpm) &
            (df["HeartRate"] < upper_bpm)
        ]["Zeitdifferenz in s"].sum()

        Durchschnittsleistung_in_zone = df[
                (df["HeartRate"] >= lower_bpm) &
                (df["HeartRate"] < upper_bpm)
            ]["PowerOriginal"].mean()

        results.append({
            "Zone": zone_name,
            "Bereich": f"{lower_bpm:.0f}–{upper_bpm:.0f} bpm",
            "Zeit in s": time_in_zone_s,
            "Zeit in min": time_in_zone_s / 60,
            "Durchschnittsleistung [W]": Durchschnittsleistung_in_zone
        })

    result_df = pd.DataFrame(results)

    return result_df



    

  