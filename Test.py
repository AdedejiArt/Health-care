
#Adio Roheen

import unittest

from Allclasses import *






if __name__ == "__main__":
    unittest.main()


class Testinsurancepluto(unittest.TestCase):
    def test_New(self):
        Insurance1=Insurance(1,"Detty December","Yearly",[])
        Insurance2=Insurance(2,"Detty","Monthly",[])
        self.assertNotEqual(Insurance1.InsurancePlan,1)
        self.assertNotEqual(Insurance2.InsurancePlan,2)


    def test_InsuranceID(self):
        Insurance1 = Insurance(1, "Delight", "Yearly",[])
        Insurance2 = Insurance(2, "Gold", "Monthly",[])

        self.assertEqual(Insurance1.InsuranceID, 1)
        self.assertEqual(Insurance2.InsuranceID, 2)

        Insurance1.InsuranceID = 12
        Insurance2.InsuranceID = 10

        self.assertEqual(Insurance1.InsuranceID, 12)
        self.assertEqual(Insurance2.InsuranceID, 10)

    def test_InsuranceName(self):
        Insurance1 = Insurance(1, "UK DELIGHT", "Yearly",[])
        Insurance2 = Insurance(2, "Gold", "Monthly",[])
        self.assertEqual(Insurance1.InsuranceName, "UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceName, "Gold")
        Insurance1.InsuranceName="Express"
        Insurance2.InsuranceName="Zenith"
        self.assertEqual(Insurance1.InsuranceName, "Express")
        self.assertEqual(Insurance2.InsuranceName, "Zenith")




    def test_WrongInsuranceName(self):
        Insurance1 = Insurance(1, "UK DELIGHT", "Yearly",[])
        Insurance2 = Insurance(2, "Gold", "Monthly",[])
        self.assertEqual(Insurance1.InsuranceName, "UK DELIGHT")
        self.assertEqual(Insurance2.InsuranceName, "Gold")

        self.assertNotEqual(Insurance1.InsuranceName, 123)
        self.assertNotEqual(Insurance2.InsuranceName, 4657)

    def test_WrongInsuranceID(self):
        Insurance1 = Insurance(1, "UK DELIGHT", "Yearly",[])
        Insurance2 = Insurance(2, "Gold", "Monthly",[])
        self.assertNotEqual(Insurance1.InsuranceID, "Mafo")
        self.assertNotEqual(Insurance2.InsuranceName, "GUI")


if __name__ == "__main__":
    unittest.main()



class TestHospital(unittest.TestCase):
    def test_HospitalName(self):
        Hospital2=Hospital("ICH","Tokyo","AOQ12","Public",["Goldberg","UK INSURANCE","Ifeoma"],25,29,["Dr Adedeji,Padaetrician","Dr Yemi,Optician","Dr Awopegba,Surgeon"],5,["Dentistry","Optical Services"])
        Hospital3=Hospital("Redmond","Oyo","A1234","private",["Midhealth","Made in Lagos","Gyrate"],255,145,["Dr Bayo,Optometrist","Dr Busrat,Nephrologist"],4,["Optical services","Dentistry","ENT","SURGERY"])
        self.assertEqual(Hospital2.Name,"ICH")
        self.assertEqual(Hospital3.Name,"Redmond")

        Hospital2.Name="Highland"
        Hospital3.Name="Alaafia"
        self.assertEqual(Hospital2.Name,"Highland")
        self.assertEqual(Hospital3.Name,"Alaafia")
    def test_HospitalRegistration(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Registration, "AOQ12")
        self.assertEqual(Hospital3.Registration, "A1234")
        Hospital2.Registration="B134E"
        Hospital3.Registration="VE567"
        self.assertEqual(Hospital2.Registration,"B134E")
        self.assertEqual(Hospital3.Registration,"VE567")
    def test_WrongName(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Name,"ICH")
        self.assertEqual(Hospital3.Name,"Redmond")

        self.assertNotEqual(Hospital2.Name,8908)
        self.assertNotEqual(Hospital3.Name,6789)
    def test_WrongRegistion(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Registration,"AOQ12")
        self.assertEqual(Hospital3.Registration,"A1234")

        self.assertNotEqual(Hospital2.Registration,11234)
        self.assertNotEqual(Hospital3.Registration,2367)
    def test_Rating(self):
        Hospital2 = Hospital("ICH", "Tokyo", "AOQ12", "Public", ["Goldberg", "UK INSURANCE", "Ifeoma"], 25, 29,
                             ["Dr Adedeji,Padaetrician", "Dr Yemi,Optician", "Dr Awopegba,Surgeon"], 5,
                             ["Dentistry", "Optical Services"])
        Hospital3 = Hospital("Redmond", "Oyo", "A1234", "private", ["Midhealth", "Made in Lagos", "Gyrate"], 255, 145,
                             ["Dr Bayo,Optometrist", "Dr Busrat,Nephrologist"], 4,
                             ["Optical services", "Dentistry", "ENT", "SURGERY"])
        self.assertEqual(Hospital2.Ratings,5)
        self.assertEqual(Hospital3.Ratings,4)

        self.assertNotEqual(Hospital2.Ratings,"Ife")
        self.assertNotEqual(Hospital3.Ratings,"Dan8i")





