import pandas as pd
import numpy as np
import plotly.express as px


def read_my_activities_csv():
    df = pd.read_csv(r"data/activities/activity.csv")
    return df


def create_window_sizes(df):
    windows_list = list(range(1, len(df) + 1))
    return windows_list




def find_best_effort(df, window_size):
    best_effort = df["PowerOriginal"].rolling(window=window_size).mean()

    best_effort_max = best_effort.max()
    return best_effort_max


def create_PC_df(df, windows_list, sampling_interval=1):
    results = []

    for window in windows_list:
        best_effort_max = find_best_effort(df, window_size=window)

        results.append({"Time": window * sampling_interval,"Power": best_effort_max})

    pc_df = pd.DataFrame(results)

    return pc_df


def plot_power_curve(pc_df):
    fig = px.line(
        pc_df,
        x="Time",
        y="Power",
        title="Power Curve",
        labels={
            "Time": "Zeit in Sekunden",
            "Power": "Best Effort Leistung in Watt"
        }
    )
    fig.show()


if __name__ == "__main__":
    df = read_my_activities_csv()

    windows_list = create_window_sizes(df)

    pc_df = create_PC_df(
        df,
        windows_list,
        sampling_interval=1
    )

    print(pc_df)

    plot_power_curve(pc_df)

    