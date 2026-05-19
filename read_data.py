import json

# Opening JSON file
file = open("data/person_db.json")

# Loading the JSON File in a dictionary
person_data = json.load(file)

person_data

import json


def load_person_data():
    file = open("data/person_db.json", encoding="utf-8")
    person_data = json.load(file)
    file.close()
    return person_data


def get_person_list(person_data):
    person_names = []

    for person in person_data:
        name = person["lastname"] + ", " + person["firstname"]
        person_names.append(name)

    return person_names




def find_person_data_by_name(suchstring):
    """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
    und die die Person als Dictionary zurück gibt"""

    person_data = load_person_data()
    #print(suchstring)
    if suchstring == "None":
        return {}

    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    for eintrag in person_data:
        print(eintrag)
        if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
            print()

            return eintrag
    else:
        return {}


