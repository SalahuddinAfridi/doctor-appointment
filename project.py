class User:
    def __init__(self, username, passward):
        self.username = username
        self.passward = passward


class Doctor:
    def __init__(self, patient, checked, unchecked, specialization, avaliability):
        self.patient = patient
        self.checked = checked
        self.unchecked = unchecked
        self.specialization = specialization
        self.avaliability = avaliability


registered_user = []
doctors = []


def register():
    print("Register yourself\n")
    username = input("Enter username :")
    passward = input("enter passward :")
    user = (username, passward)
    registered_user.append(user)
    print("Registration successfully\n\n")


def login():
    print("please login\n")
    username = input("Enter username :")
    passward = input("Enter passward :")
    for user in registered_user:
        if user == username and passward == passward:
            print("login successful")
        return
    print("invalid username or passward")


def view_doctors():
    print("Avaliable Doctors")
    file = open('geek.txt', 'r')
    for each in file:
        print(each)
    for doctor in doctors:
        print(f"Nmae:{doctor.name}\t avaliability : {doctor.avaliability}")
        print(
            f"Name : {doctor.name}\t specialization : {doctor.specialization}")


def view_doctor_details():
    doctor_name = input("enter doctor name : ")
    for doctor in doctors:
        if doctor.name == doctor_name:
            print(f"specialization : {doctor.specialization}")
            print(f"avaliability : {doctor.avaliability}")
        return
    print("Doctor not found")


class Admin:
    def _init_(self):
        self.patients = []
        self.doctors = []

    def register_patient(self, patient):
        self.patients.append(patient)
        print("Patient registered successfully.")

    def book_appointment(self, patient_id, doctor_id, date_time):
        patient = self.get_patient(patient_id)
        doctor = self.get_doctor(doctor_id)

        if patient and doctor:
            appointment = {"patient": patient,
                           "doctor": doctor, "date_time": date_time}
            patient.appointments.append(appointment)
            doctor.appointments.append(appointment)
            print("Appointment booked successfully.")
        else:
            print("Invalid patient or doctor ID.")

    def get_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def get_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def view_all_patients(self):
        for patient in self.patients:
            print(f"ID: {patient.id}\tName: {patient.name}")

    def view_all_doctors(self):
        for doctor in self.doctors:
            print(f"ID: {doctor.id}\tName: {doctor.name}")


# print("1: SignUp\n2: Login\n")
# opt = input("Enter a number accordingly: ")
# if (opt == "1"):
#     print(Doctor())
# elif opt == "2":
#     print(Doctor(login(), view_doctors()))
# else:
#     print("INVALID OPTION!")


print(Doctor(register(), login(), view_doctors(), view_doctor_details()))
# my_object = Admin()
# my_object.register_patient()
# my_object. book_appointment()
# my_object.get_patient()
# my_object.get_doctor()
# my_object.view_all_patients()
# my_object.view_all_doctors()
