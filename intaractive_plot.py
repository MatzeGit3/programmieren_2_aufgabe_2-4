import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import read_my_activity, make_hr_plot

# Wo startet sie Zeitreihef
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

with tab2:
    st.header("Power-Data")
    st.write("# HR")

    df = read_my_activity()
    fig = make_power_hr_plot(df)
    st.plotly_chart(fig)
