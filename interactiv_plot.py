import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from sort import bubble_sort
from read_pandas import read_my_activities_csv
from read_pandas import make_plot_power
from read_pandas import power_max   
from read_pandas import power_mean
from read_pandas import add_Hr_Zone


# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)
    hr_max = 190    
    Zone_1_df, Zone_2_df, Zone_3_df, Zone_4_df, Zone_5_df = add_Hr_Zone(df, hr_max)
    st.write("Zone 1:", Zone_1_df)
    st.write("Zone 2:", Zone_2_df)
    st.write("Zone 3:", Zone_3_df)
    st.write("Zone 4:", Zone_4_df)
    st.write("Zone 5:", Zone_5_df)
with tab2:
    st.header("Power-Data")
    df = read_my_activities_csv()
    fig = make_plot_power(df)
    st.plotly_chart(fig)
    st.write("Maximale Power:", power_max(df))
    st.write("Durchschnittliche Power:", power_mean(df))
    