doctors = []
class patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def getinfo(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def assign_doctor(self):
    
        print("Available Doctors:")
        for i, doctor in enumerate(doctors):
            print(f"{i+1}. {doctor.name} - {doctor.specialty}")
        choice = input("Enter the number of the doctor you want to assign: ")
        self.doctor = doctors[int(choice) - 1]
        doctor[int(choice)-1].patients.append(self)

class doctor:
    def __init__(self, name, age, gender, specialty):
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = specialty
        self.patients = []

    def getinfo(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def display_patients(self):
        print(f"Patients assigned to {self.name}:")
        for patient in self.patients:
            print(patient.name)

doc1 = doctor("John","30","Male","Cardiology")
doc2 = doctor("Susan","55","Female","Dentist")
doctors.append(doc1)
doctors.append(doc2)
n = int(input("Enter number of patients"))
for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    patient = patient(name, age, gender)
    patient.assign_doctor()
    print(patient.getinfo())
    print("Doctor details:")
    print(patient.doctor.getinfo())