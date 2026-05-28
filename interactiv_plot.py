import streamlit as st
import read_pandas as rp





st.header("Heartrate and Power Data")
st.write("# My Plot")
max_heart_rate = st.number_input(
    "Maximale Herzfrequenz eingeben",
    min_value=100,
    max_value=250,
    value=190,
    step=1
)

st.write("Deine maximale Herzfrequenz ist:", max_heart_rate)
df = rp.read_my_activities_csv()
fig = rp.make_power_and_hr_plot(df, max_heart_rate, zones=rp.zones())
st.plotly_chart(fig)
st.write("Zeit in Herzfrequenzzonen:")
time_in_zones = rp.time_in_heart_rate_zones(df, max_heart_rate, zones=rp.zones())
st.write(time_in_zones)
st.write("Durchschnittliche Herzfrequenz:", rp.power_mean(df["HeartRate"]))
st.write("Maximale Herzfrequenz:", rp.power_max(df["HeartRate"]))
st.write("Durchschnittliche Leistung:", rp.power_mean(df["PowerOriginal"]))


    
   


    