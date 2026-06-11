import json
from PIL import Image


class Person:

    @staticmethod
    def load_person_data():
        """
        Lädt die Personendaten aus der JSON-Datei
        und gibt eine Liste von Person-Objekten zurück.
        """
        with open("data/person_db.json", "r", encoding="utf-8") as file:
            person_data = json.load(file)

        person_object_list = []

        for person_dict in person_data:
            person_object = Person(
                person_dict["id"],
                person_dict["date_of_birth"],
                person_dict["firstname"],
                person_dict["lastname"],
                person_dict["picture_path"],
                person_dict["ekg_tests"],
                person_dict["gender"]
            )

            person_object_list.append(person_object)

        return person_object_list


    @staticmethod
    def get_person_list(persons):
        """
        Erstellt eine Liste mit allen Namen der Personen.
        """
        person_names = []

        for person in persons:
            person_names.append(person.get_full_name())

        return person_names


    @staticmethod
    def find_person_data_by_name(full_name):
        """
        Sucht eine Person anhand des Namens im Format:
        'Nachname, Vorname'
        und gibt das passende Person-Objekt zurück.
        """
        persons = Person.load_person_data()

        lastname = full_name.split(", ")[0]
        firstname = full_name.split(", ")[1]

        for person in persons:
            if person.firstname == firstname and person.lastname == lastname:
                return person

        return None
    
    
    @staticmethod
    def load_by_id(person_id):
        """
        Sucht eine Person anhand der ID
        und gibt das passende Person-Objekt zurück.
        """
        persons = Person.load_person_data()

        for person in persons:
            if person.id == person_id:
                return person
            
        return None

   

    def __init__(self, id : int, date_of_birth : int, firstname, lastname, picture_path, ekg_tests, gender = "Male"):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests
        self.gender = gender
        self.hr_max = self.calc_max_heart_rate()
       



    def calc_age(self):
        """
        Berechnet das Alter aus dem Geburtsjahr.
        """
        age = 2026 - int(self.date_of_birth)
        return age

    def calc_max_heart_rate(self):
     
     """
     Berechnet die maximale Herzfrequenz.
        """
     age = self.calc_age()

     if self.gender.lower() == "female":
        max_heart_rate = 226 - age
     else:
        max_heart_rate = 220 - age

     return max_heart_rate


    def set_hr(self, hr):
        self.hr_max = hr

    def get_full_name(self):
        return self.lastname + ", " + self.firstname


    def get_image(self):
        image = Image.open(self.picture_path)
        return image
    



if __name__ == "__main__":


    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    person = Person.find_person_data_by_name("Huber, Julian")

    print(person.get_full_name())
    print(person.calc_age())
    print(person.calc_max_heart_rate())