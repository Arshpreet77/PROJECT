

import modules

DATA_DOCTORS_FILE = "doctors.txt"
DATA_PATIENTS_FILE = "patients.txt"

# doctors function 
def display_dr_menu():
    # display menu
    print()
    print("ARH Management System")
    print("    Doctor's Menu\n")
    print("1 - List of Doctors ")
    print("2 - Search for Doctor by ID ")
    print("3 - Search for Doctor by Name/Partial Name ")
    print("4 - Add new Doctor ")
    print("5 - Edit Doctor Info ")
    print("0 - Return to Main Menu")

def manage_dr():

    display_dr_menu()
    # initialize menu option
    menu_option = "11"
    dr_list = []
    # Read the list of doctors from file and store it in the dr_list variable
    dr_list = read_doctors_file()
    # loop until user enters 0 to exit
    while menu_option != "0":
        menu_option = input("Enter option: ")
        if menu_option == "1":
            print()
            display_list_of_drs(dr_list)
        elif menu_option == "2":
            print()
            dr_id = int(input("Enter the doctor ID: "))
            if find_dr_by_id(dr_id, dr_list) == -1:
                print(f"Doctor with ID {dr_id} not found")
        elif menu_option == "3":
            print()
            match_dr_by_name(dr_list)
        elif menu_option == "4":
            print()
            add_dr_to_list(dr_list)
        elif menu_option == "5":
            print()
            edit_dr_info(dr_list)
            # print doctor list
            display_list_of_drs(dr_list)
        display_dr_menu()
    # write doctors file
    write_drs_list_to_file(dr_list)

def read_doctors_file():
    #This function reads the data from the doctors.txt file and returns a list of doctor objects.
    dr_list = []
    with open(DATA_DOCTORS_FILE, "r") as dr_file:

        next(dr_file)    
        for line in dr_file:
            line = line.strip()
            dr_data = line.split("_")
            dr_obj = modules.Doctor(dr_data[0], dr_data[1], dr_data[2], dr_data[3], dr_data[4], dr_data[5])
            dr_list.append(dr_obj)
    return dr_list

def find_dr_by_id(dr_id, dr_list):
#This function searches the doctor list for a doctor with the given ID
    for dr in dr_list:
        if dr.get_id() == dr_id:
            print(dr)
            return dr
    return -1

def match_dr_by_name(dr_list):
   # A function to match the doctor by their name
    output_list = []
    input_name = input("Enter the doctor name: ")
    nbr_matches = 0
     # Loop through the doctor list
    for dr in dr_list:
        if input_name.lower() in dr.get_name().lower():
            output_list.append(dr)
            nbr_matches += 1
    if nbr_matches == 0:
        print("Not found.")
    else:
        display_list_of_drs(output_list)

def display_list_of_drs(dr_list):
 
    # print header
    print(f"{'ID':<5s} {'Name':20s} {'Specialist':20s} {'Schedule':10s} {'Qualifications':15s} {'Room Nbr':>10s}")
    for dr in dr_list:
        print(dr)

def get_new_dr_info():
    
    dr_name = input("Enter Dr name: ")
    dr_specialty = input("Enter Dr specialty: ")
    dr_schedule = input("Enter Dr schedule: ")
    dr_qualifications = input("Enter Dr qualifications: ")
    dr_room_number = input("Enter Dr room number: ")
    dr = modules.Doctor(0, dr_name, dr_specialty, dr_schedule, dr_qualifications, dr_room_number)
    return dr

def add_dr_to_list(dr_list):
   
    dr_id = int(input("Enter Dr ID: "))
    dr = find_dr_by_id(dr_id, dr_list)
    if dr != -1:
        print(f'Doctor with id {dr_id} already exists - cannot add')
    else:
        dr = get_new_dr_info()
        dr.set_id(dr_id)
        dr_list.append(dr)
        print(f'Doctor with id {dr_id} successfully added')

def write_drs_list_to_file(dr_list):
    #This function takes in a list of doctor objects and writes their attributes to a file in a specific format
#The file is opened in write mode, meaning it will overwrite any existing content
    with open(DATA_DOCTORS_FILE, "w") as dr_file:
        dr_file.write("ID_Name_Specialist_Schedule_Qualifications_Room Nbr\n")
        for dr in dr_list:
            dr_file.write(f'{dr.get_id()}_{dr.get_name()}_{dr.get_specialty()}_{dr.get_schedule()}_{dr.get_qualification()}_{dr.get_room_number()}\n')

def edit_dr_info(dr_list):
    
    dr_id = int(input("Enter the doctor ID to edit: "))
    new_dr = find_dr_by_id(dr_id, dr_list)
    if new_dr == -1:
        print("Doctor ID not found.")
    else:
        new_dr = get_new_dr_info()
        new_dr.set_id(dr_id)
        # edit dr information
        for dr in dr_list:
            if dr.get_id() == dr_id:
                dr.set_name(new_dr.get_name())
                dr.set_specialty(new_dr.get_specialty())
                dr.set_schedule(new_dr.get_schedule())
                dr.set_qualification(new_dr.get_qualification())
                dr.set_room_number(new_dr.get_room_number())
        print(f"Dr with ID {dr_id} successfully modified.")

# Patients Management functions
def display_patients_menu():
    # display menu
    print()
    print("ARH Management System")
    print("    Patinets's Menu\n")
    print("1 - List of Patients ")
    print("2 - Search for Patients by ID ")
    print("3 - Add new Patients ")
    print("4 - Edit Patients Info ")
    print("0 - Return to Main Menu")

def manage_patients():
    

    # display menu
    display_patients_menu()
    # initialize menu option
    menu_option = "11"
    # initialize patients list
    list_of_patients = []
    # read patinets file
    list_of_patients = read_patients_file()
    # loop until user enters 0 to exit
    while menu_option != "0":
        menu_option = input("Enter option: ")
        if menu_option == "1":
            display_patient_list(list_of_patients)
        elif menu_option == "2":
            patients_id = int(input("Enter the patients ID: "))
            if find_patients_by_id(patients_id, list_of_patients) == -1:
                print(f"Patients with ID {patients_id} not found")
        elif menu_option == "3":
            add_patient_to_list(list_of_patients)
        elif menu_option == "4":
            edit_Patient_info(list_of_patients)
            # print patients list
            display_patient_list(list_of_patients)
        display_patients_menu()
    # write doctors file
    write_patients_file(list_of_patients)

def read_patients_file():
    #This function reads the patients' data from a file and creates a list of patient objects.
    patients_list = []
    with open(DATA_PATIENTS_FILE, "r") as patients_file:
        # avoid the first header line
        next(patients_file)
        for line in patients_file:
            line = line.strip()
            #A new Patient object is created using the data, and then appended to the patients_list.
            patients_data = line.split("_")
            patients_obj = modules.Patient(
                patients_data[0], patients_data[1], patients_data[2], patients_data[3], patients_data[4], )
            patients_list.append(patients_obj)
    return patients_list

def find_patients_by_id(patients_id, patients_list):
    #This function takes a patient ID and a list of patient objects as input.
#It then searches the list of patient objects to find the patient with the given ID.
    for patients in patients_list:
        if patients.get_id() == patients_id:
            print(patients)
            return patients
    return -1

def display_patient_list(display_list_of_patients):
#This function takes a list of patient objects as input.
#It then iterates through the list and prints the details of each patient object.
    for patients in display_list_of_patients:
        print(patients)

def get_new_Patient_info():
    
    patients_name = input("Enter patient name: ")
    patients_diagnosis = input("Enter patient diagnosis: ")
    patients_gender = input("Enter patient gender: ")
    patients_age = input("Enter patient age: ")
    patient = modules.Patient(
        0, patients_name, patients_diagnosis, patients_gender, patients_age)
    return patient

def add_patient_to_list(patient_list):
    # This function adds a new patient to the patient list.
# It takes a list of patients as input.
    patient_id = int(input("Enter Patient ID: "))
    patient = find_patients_by_id(patient_id, patient_list)
    if patient != -1:
        print(f'Patient with id {patient_id} already exists - cannot add')
    else:
        patient = get_new_Patient_info()
        patient.set_id(patient_id)
        patient_list.append(patient)
        print(f'Patient with id {patient_id} successfully added')

def write_patients_file(patients_list):
    # This function writes the patient list to the patient data file.
# It takes a list of patients as input.
    with open(DATA_PATIENTS_FILE, "w") as patients_file:
        patients_file.write("ID_Name_Diagnosis_Gender_Age\n")
        for patient in patients_list:
            patients_file.write(
                f'{patient.get_id()}_{patient.get_name()}_{patient.get_diagnosis()}_{patient.get_gender()}_{patient.get_age()}\n')

def edit_Patient_info(patients_list):
    patients_id = int(input("Enter the Patient ID to edit: "))
    found = False
    for patient in patients_list:
        if patient.get_id() == patients_id:
            found = True
            new_patient = get_new_Patient_info()
            new_patient.set_id(patients_id)
            patient.set_name(new_patient.get_name())
            patient.set_diagnosis(new_patient.get_diagnosis())
            patient.set_gender(new_patient.get_gender())
            patient.set_age(new_patient.get_age())
            print(f"Patient with ID {patients_id} successfully modified.")
            break
    if not found:
        print("Patient ID not found.")

def display_main_menu():
    print("\nARH Management System\n    Main Menu\n\n1 - Doctor \n2 - Patient \n0 - Close Application")

def main():
    
    main_menu_option = ""

    display_main_menu()

    while main_menu_option != "0":

        main_menu_option = input("Enter option: ")
        if main_menu_option == "1":
            manage_dr()
            display_main_menu()
        elif main_menu_option == "2":
            manage_patients()
            display_main_menu()

    print("ARH Management System successfully closed")

if __name__ == "__main__":
    main()
    exit(0)