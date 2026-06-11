import streamlit as st

from person import Person
from ekgdata import EKGdata

st.title("EKG App")

persons = Person.load_person_data()
person_names = Person.get_person_list(persons)

col1, col2 = st.columns(2)

with col1:
    st.write("## Versuchsperson auswählen")

    current_user = st.selectbox(
        "Versuchsperson", options=person_names, key="sbVersuchsperson"
    )

    current_person = Person.find_person_data_by_name(current_user)

    st.write(f"**Name:** {current_person.get_full_name()}")
    st.write(f"**Geburtsjahr:** {current_person.date_of_birth}")
    st.write(f"**Alter:** {current_person.calc_age()}")
    st.write(f"**Geschlecht:** {current_person.gender}")
    st.write(f"**Maximale Herzfrequenz:** {current_person.calc_max_heart_rate()} bpm")

with col2:
    image = current_person.get_image()
    st.image(image, caption=current_person.get_full_name())


st.write("---")

col3, col4 = st.columns([1, 2])

with col3:
    st.write("## EKG-Test auswählen")

    ekg_tests = current_person.ekg_tests

    ekg_options = []

    for ekg_test in ekg_tests:
        option_text = f"ID {ekg_test['id']} - {ekg_test['date']}"
        ekg_options.append(option_text)

    selected_ekg_text = st.selectbox("EKG-Test", options=ekg_options, key="sbEKGTest")

    selected_ekg_id = int(selected_ekg_text.split(" ")[1])

    ekg = EKGdata.load_by_id(selected_ekg_id)

    if ekg is not None:
        peaks = ekg.find_peaks()
        avg_hr = ekg.calculate_avg_hr()

        st.write(f"**EKG-ID:** {ekg.id}")
        st.write(f"**Datum:** {ekg.date}")
        st.write(f"**Anzahl Peaks:** {len(peaks)}")
        st.write(f"**Durchschnittliche Herzfrequenz:** {avg_hr}")

with col4:
    if ekg is not None:
        fig = ekg.plot_time_series()
        st.plotly_chart(fig)
    else:
        st.write("EKG wurde nicht gefunden.")
