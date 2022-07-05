#The author of the code is Adio Adedeji
#Class of PrivatePatients
class PrivatePatients:
    def __init__(self,Name,Age,Gender,Identification,Nationality,Occupation):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Identification=Identification
        self.Nationality=Nationality
        self.Occupation=Occupation
        print("A new patient has joined")
    def __repr__(self):
        return "Object :{} ".format(self.Name)
