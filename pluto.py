#The author of the code is Adio Adedeji
#This is the Class Hospital
class Hospital:
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctor,NumberofNurses,Ratings,Services):
        self.Name=Name
        self.Location=Location
        self.Registration=Registration
        self.Ownership=Ownership
        self.Insurance=Insurance
        self.NumberofDoctor=NumberofDoctor
        self.NumberofNurses=NumberofNurses
        self.Ratings=Ratings
        self.Services=Services
        print("A new Hospital has been added,Welcome officially to our team")

    def __repr__(self):
        return 'Hospital Name: {} '.format(self.Name)
# A list of hospitals(Objects) were created
hospital=[]
Hospital2 = Hospital("ICH", "Tokyo", "A0056", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29, 5,
                         ["Dentistry", "Optical Services"])
hospital.append(Hospital2)
Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145, 4,
                         ["Optical services", "Dentistry", "ENT", "SURGERY"])
hospital.append(Hospital3)


#This is an inheritance of Hospital
class Doctors(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services,DoctorName,Specialization,Gender):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services)
        self.DoctorName=DoctorName
        self.Specialization=Specialization
        self.Gender=Gender
    def __repr__(self):
        return 'Hospital Name: {} '.format(self.Name)

#Also an inheritance
class Insurance(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services,InsuranceName,ID):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services)
        self.InsurannceName=InsuranceName
        self.ID=ID
#Also an Inheritance
class Patient(Hospital):
    def __init__(self,Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services,NOP,Ailment,Detection,Terminal):
        super().__init__(Name,Location,Registration,Ownership,Insurance,NumberofDoctors,NumberofNurses,Ratings,Services)
        self.Nop=NOP
        self.Ailment=Ailment
        self.Detection=Detection
        self.Terminal=Terminal
        print("A new patient has been added")



