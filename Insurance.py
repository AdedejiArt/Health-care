#The author of the code is Adio Adedeji
class Insurance:
    def __init__(self,InsuranceName,InsurancePlan,InsuranceID,Subscribers):
        self.InsuranceName=InsuranceName
        self.InsurancePlan=InsurancePlan
        self.InsuranceID=InsuranceID
        self.Subscribers=Subscribers
        print("An insurance Company has joined")
    def __repr__(self):
        return "Insurance Name: {}".format(self.InsuranceName)
    def Add(self):
        print("You have been added to our List")
insurance=[]

Insurance1 = Insurance("Health Line", "Yearly", 121, ["Babalola", "Ella", "Adedeji"])
Insurance2 = Insurance("Policy", "Monthly", 100, ["Burna", "Damini", "Steph London"])
Insurance1List = []
Insurance1List.append(Insurance1.Subscribers)
Insurance2List = []
Insurance2List.append(Insurance2.Subscribers)
insurance.append(Insurance1)
insurance.append(Insurance2)









