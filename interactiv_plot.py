import streamlit as st
import read_pandas as rp
import plotly.express as px
from advanced_powercurve import read_data, add_timer, create_power_curve_dataframe

df = rp.read_my_activities_csv()
HR_max = rp.power_max(df["HeartRate"])
st.header("Heartrate and Power Data")
st.write("# My Plot")
max_heart_rate = st.number_input(
    "Maximale Herzfrequenz eingeben",
    min_value=HR_max,
    max_value=250,
    value=HR_max,
    step=1,
)

st.write("Deine maximale Herzfrequenz ist:", max_heart_rate)
fig = rp.make_power_and_hr_plot(df, max_heart_rate, zones=rp.zones())
st.plotly_chart(fig)
st.write("Zeit in Herzfrequenzzonen:")
time_in_zones = rp.time_in_heart_rate_zones(df, max_heart_rate, zones=rp.zones())
st.write(time_in_zones)
st.write("Durchschnittliche Herzfrequenz:", rp.power_mean(df["HeartRate"]))
st.write("Maximale Herzfrequenz:", rp.power_max(df["HeartRate"]))
st.write("Durchschnittliche Leistung:", rp.power_mean(df["PowerOriginal"]))
st.write("Maximale Leistung:", df["PowerOriginal"].max())


st.header("Power Curve")

df = add_timer(df)

power_curve_df = create_power_curve_dataframe(df)
power_curve_plot_df = power_curve_df.dropna()

fig_power_curve = px.line(
    power_curve_plot_df,
    x="Zeit in Sekunden",
    y="Best Effort Leistung [W]",
    markers=True,
    title="Power Curve",
)

fig.update_xaxes(
    tickvals=[10, 20, 30, 60, 300, 600, 1200, 1800],
    ticktext=["10s", "20s", "30s", "1min", "5min", "10min", "20min", "30min"],
)

st.plotly_chart(fig_power_curve)
