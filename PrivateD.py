#The author of the code is Adio Adedeji
#Class Private Doctors
class PrivateDoctors:
    def __init__(self,Name,ID,Qualification,gender,Clinicofwork,ratings,articles):
        self.Name=Name
        self.ID=ID
        self.Qualification=Qualification
        self.gender=gender
        self.Clinicofwork=Clinicofwork
        self.ratings=ratings
        self.articles=articles
        print("A new Doctor has been Created")
    def __repr__(self):
        return "Private Doctor :{}".format(self.Name)
Doctor=PrivateDoctors("Adedeji","0012A","Padaetrician","M","Oleku",5,[])
Doctor1=PrivateDoctors("Aderinsola","0234","ENT DOCTOR","F","Highland",4,[])
Doctor2=PrivateDoctors("Adeolu","0045","Surgeon","M","Alaafia",3,[])
doctor=[]
doctor.append(Doctor1.Name)
doctor.append(Doctor.Name)
doctor.append(Doctor2.Name)
