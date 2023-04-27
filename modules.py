
class Doctor:
    def __init__(self, doctor_id = 0, name = "", specialty = "", schedule = "", qualification = "", room_number = ""):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialty = specialty
        self.__schedule = schedule
        self.__qualification = qualification
        self.__room_number = room_number

    def get_doctor_id(self):
        return self.__doctor_id

    def set_doctor_id(self, new_id):
        self.__doctor_id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_specialty(self):
        return self.__specialty

    def set_specialty(self, new_specialty):
        self.__specialty = new_specialty

    def get_schedule(self):
        return self.__schedule

    def set_schedule(self, new_schedule):
        self.__schedule = new_schedule

    def get_qualification(self):
        return self.__qualification

    def set_qualification(self, new_qualification):
        self.__qualification = new_qualification

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, new_room_number):
        self.__room_number = new_room_number

    def format_file_layout(self):
        return str(self.__doctor_id) + "_" + self.__name + "_" + self.__specialty + "_" + self.__schedule + "_" + self.__qualification + "_" + self.__room_number

    def __str__(self):
        output = f"{self.__doctor_id:<5d} {self.__name:20s} {self.__specialty:20s} {self.__schedule:10s} {self.__qualification:15s} {self.__room_number:>10s}"
        return output
    
class Patient:
    def __init__(self, patient_id = 0, name = "", diagnosis = "", gender = "", age = 0):
        self.__patient_id = patient_id
        self.__name = name
        self.__diagnosis = diagnosis
        self.__gender = gender
        self.__age = age

    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, new_id):
        self.__patient_id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_diagnosis(self):
        return self.__diagnosis

    def set_diagnosis(self, new_diagnosis):
        self.__diagnosis = new_diagnosis

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):
        self.__gender = new_gender

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
    
    def format_file_layout(self):
        return str(self.__patient_id) + "_" + self.__name + "_" + self.__diagnosis + "_" + self.__gender + "_" + str(self.__age)
    
    def __str__(self):
        output = f"{self.__patient_id:<5d} {self.__name:20s} {self.__diagnosis:20s} {self.__gender:10s} {self.__age:3d}"
        return output
    
def main():

    doctor1 = Doctor(doctor_id = 1, name = "Dr. Smith", specialty = "Cardiology", schedule = "9AM-5PM", qualification = "MBBS", room_number = "A101")
    print(doctor1)

    print(doctor1.format_file_layout())
    print()
    
    patient1 = Patient(patient_id = 1, name = "Pankaj", diagnosis = "Cancer", gender = "Male", age = 30)
    print(patient1)


    print(patient1.format_file_layout())
    print()
    
    patient2 = Patient()
    patient2.set_patient_id(2)
    patient2.set_name("Sumit")
    patient2.set_diagnosis("Covid")
    patient2.set_gender("Male")
    patient2.set_age(23)

    print(f'{"ID":5s} {"Name":20s} {"Diagnosis":20s} {"Gender":10s} {"Age":3s}')
    print(patient2)

    print(patient2.__str__())
    print()

if __name__ == "__main__":
    main()

