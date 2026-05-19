import streamlit as st
import read_data as read_data

# Daten aus der Datei laden
person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)
col1, col2 = st.columns(2)


with col1:
    st.write("# EKG APP")

    # Eine Überschrift der zweiten Ebene
    st.write("## Versuchsperson auswählen")

    # Eine Auswahlbox
    current_user = st.selectbox(
        "Versuchsperson", options=person_names, key="sbVersuchsperson"
    )
    current_person = read_data.find_person_data_by_name(current_user)
    # Auslesen des Pfades aus dem zurückgegebenen Dictionary
    current_picture_path = current_person["picture_path"]
    # Paket zum anzeigen der Bilder
    # Eine Überschrift der ersten Ebene
    st.write(f"Der Name ist: {current_user}")
    st.write(f"Der Pfad ist: {current_picture_path}")
with col2:
    from PIL import Image
    # Laden eines Bilds
    image = Image.open(current_picture_path)
    # Anzeigen eines Bilds mit Caption
    st.image(image)

hallo = "Hallo Welt"


