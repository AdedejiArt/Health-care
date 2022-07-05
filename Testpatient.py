import unittest
from patients import *
from PrivateD import*


class Testpatient(unittest.TestCase):
    def test_Newperson(self):
        Patient1 = PrivatePatients("Ayo", 12, "Male", "a123", "Nigerian", "Computer scientist")
        Patient2 = PrivatePatients("Bolanle", 13, "Female", "QWEQ12", "Ghanian", "Sceintist")
        Patient1.Name = "Ayo"
        Patient2.Name = "Bolanle"
        self.assertEqual(Patient1.Name, "Ayo")
        self.assertEqual(Patient2.Name, "Bolanle")

    def test_Age(self):
        Patient1=PrivatePatients("Ayo",12,"Male","a123","Nigerian","Computer Scientist")
        Patient1.Age=12
        self.assertEqual(Patient1.Age,12)

    def test_Gender(self):
        Patient1 = PrivatePatients("Ayo", 12, "Male", "a123", "Nigerian", "Computer Scientist")
        Patient1.Gender = "Male"
        self.assertEqual(Patient1.Gender,"Male")
    def test_RegistrationID(self):
        Patient1 = PrivatePatients("Ayo", 12, "Male", "a123", "Nigerian", "Computer Scientist")
        Patient1.Identification = "a123"
        self.assertEqual(Patient1.Identification, "a123")
    def test_NotRegistrationID(self):
        Patient1 = PrivatePatients("Ayo", 12, "Male", "a123", "Nigerian", "Computer Scientist")
        Patient1.Identification = "a123"
        self.assertNotEqual(Patient1.Identification, "Ngerian")

class TestPrivateDoctors(unittest.TestCase):
    def test_Name(self):
        PrivateD1=PrivateDoctors("Adedeji","AQ12","Surgeon","Male","Redmond",5,"Nil")
        PrivateD1.Name="Adedeji"
        self.assertEqual(PrivateD1.Name,"Adedeji")
    def test_Identification(self):
        PrivateD1 = PrivateDoctors("Adedeji", "AQ12", "Surgeon", "Male", "Redmond", 5, "Nil")
        PrivateD1.ID = "AQ12"
        self.assertEqual(PrivateD1.ID, "AQ12")
    def test_Gender(self):
        PrivateD1 = PrivateDoctors("Adedeji", "AQ12", "Surgeon", "Male", "Redmond", 5, "Nil")
        PrivateD1.Gender = "Male"
        self.assertEqual(PrivateD1.Gender, "Male")






