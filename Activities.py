# The author of the Code is Adio Adedeji
from pluto import *
from Insurance import *
from PrivateD import *
from patients import *
import datetime
name=input("What is your name")
filename=name
with open(filename,"a") as f:
    f.write("This is the file for"+filename)

# We welcome them to the app
# We ask them to pick options based on their Goals on the app
print("Welcome to Pluto App")
Apply = int(input("Would you like to log in as\n"
                  "Press 1 for Hospital Administartor\n"
                  "Press 2 for Insurance Plan\n"
                  "Press 3 for a private Doctor\n"
                  "Press 4 for a patient"))
# if Option 1 is picked,It means we will as our users Hospital management related questions
if Apply == 1:
    repeat_actions = True
    with open(filename, "a") as f:
        f.write("This file is for a Hospital administrator\n")
    with open(filename, "a") as f:
        f.write("Date : {}".format(datetime) + "\n")
    print("Welocme to our Hospital section")
    print("We look forward to working with you")
    # As the Hospita management,We ask them the options they would like to perform
    Input = int(input("We have the following activities\n"
                      " Press 1 for Joining our team\n"
                      "Press 2 for Viewing the list of hospitals\n"
                      "Press 3 for adding patients \n"

                      "Press 4 for Viewing your Insurance List"))

    # 1 is for New Users who would like to register on the portal

    if Input == 1:
        with open(filename, "a") as f:
            f.write("Input : " + "One" + "\n")
        print("Thanks for Choosing to join us")
        Name = input("What is the Name of your Hospital")
        with open(filename, "a") as f:
            f.write("Name : " + Name + "\n")
        Location = input("Where is the location of the hospital")
        with open(filename, "a") as f:
            f.write("Loaction : " + Location + "\n")
        Registration = input("What is the registration ID")
        with open(filename, "a") as f:
            f.write("Registration : " + Registration + "\n")
        Ownership = input("Is it a private or public Company")
        with open(filename, "a") as f:
            f.write("Ownership : " + Ownership + "\n")
        Insurance = input("Does your hospital have insurance registered Under it,If yes List them")
        with open(filename, "a") as f:
            f.write("Insurance: " + Insurance + "\n")
        # We ask the new user if his/her hospital is registered under any Insurance Company
        # If the answer is No,The program would end
        if Insurance == "No":
            print("You have to beregistered under an Insurance Scheme for you to be on  Pluto")
            exit("Thank You")
            # If yes,The program Would be continued
        Doc = int(input('Kindly Input the number of Doctors in your Hospital'))
        with open(filename, "a") as f:
            f.write("Doc : " + str(Doc) + "\n")
        Nurses = int(input("Kindly input the number of Nurses in your Hospital"))
        with open(filename, "a") as f:
            f.write("Nurses : " + str (Nurses) + "\n")
        Ratings = int(input("Kindly input your ratings as given on google.Ratings would be verified"))
        with open(filename, "a") as f:
            f.write("Service : " + str(Ratings) + "\n")
        Service = input("Kindly give us a list of your services")
        with open(filename, "a") as f:
            f.write("Service : " + Service + "\n")
        Service1 = input("First service")
        with open(filename, "a") as f:
            f.write("Service : " + Service1 + "\n")
        service2 = input("Second Service")
        with open(filename, "a") as f:
            f.write("Service : " + service2 + "\n")
            # We are appending the services offered by the hospital in a list
        List = []
        List.append(Service)
        List.append(Service1)
        List.append(service2)
        print("Your services are", List)
        Your = []
        Hospital1 = Hospital(Name, Location, Registration, Ownership, Insurance, Doc, Nurses, Ratings, Service)
        Your.append(Hospital1)
        print(Your)
    # They can also view the List of hospitals on our App
    elif Input == 2:
        f.write("Input : " + str(2) + "\n")
        print("Thanks for Choosing to join us")
        for x in hospital:
            print(x)

    # They can register a patient themselves
    elif Input == 3:
        f.write("Input : " + str (3) + "\n")
        Name = input("What is the Name of your Hospital")
        with open(filename, "a") as f:
            f.write("Name : " + Name + "\n")
        Location = input("Where is the location of the hospital")
        with open(filename, "a") as f:
            f.write("Location : " + Location + "\n")
        Registration = input("What is the registration ID")
        with open(filename, "a") as f:
            f.write("Registartion : " + Registration + "\n")
        Ownership = input("Is it a private or public Company")
        with open(filename, "a") as f:
            f.write("Email address : " + Ownership + "\n")
        Insurance = input("Does your hospital have insurance registered Under it")
        with open(filename, "a") as f:
            f.write("Email address : " + Insurance + "\n")
        Doc = int(input('Kindly Input the number of Doctors in your Hospital'))
        with open(filename, "a") as f:
            f.write("Email address : " + str(Doc) + "\n")
        Nurses = int(input("Kindly input the number of Nurses in your Hospital"))
        with open(filename, "a") as f:
            f.write("Email address : " + str(Nurses) + "\n")
        Ratings = int(input("Kindly input your ratings as given on google.Ratings would be verified"))
        with open(filename, "a") as f:
            f.write("Email address : " + str(Ratings) + "\n")
        Service = input("Kindly give us a list of your services")
        with open(filename, "a") as f:
            f.write("Email address : " + Service + "\n")
        patient = input("Kindly input the patients name")
        with open(filename, "a") as f:
            f.write("Email address : " + patient + "\n")
        Ailment = input("Kindly enter the Ailment of the patient")
        with open(filename, "a") as f:
            f.write("Email address : " + Ailment + "\n")
        Detection = input("Kindly enter the date the ailment was detected")
        with open(filename, "a") as f:
            f.write("Email address : " + Detection + "\n")
        Terminal = input("Is it a terminal disease")
        with open(filename, "a") as f:
            f.write("Email address : " + Terminal + "\n")
        New_Patient = Patient(Name, Location, Registration, Ownership, Insurance, Doc, Nurses, Ratings, Service,
                              patient, Ailment, Detection, Terminal)

    # This is used to view the insurance List under the Hospital
    elif Input == 4:
        f.write("Email address : " + str(4) + "\n")
        Hospital_Name = input("Kindly enter the name of your Hospital")
        if Hospital_Name == "Redmond":
            for x in Hospital2.Insurance:
                print(x)
        elif Hospital_Name == "ICH":
            for x in Hospital3.Insurance:
                print(x)

# If the User is an Insurance Company or wants to log in as an Insurance Company
elif Apply == 2:
    InsuranceWork = int(input("Enter 1 to Register as a new Insurance Company on our group\n"
                              "Enter 2 to Register a new Subscriber\n"
                              "Enter 3 to quit Your appointment with us\n"))
    repeat_actions = True
    with open(filename, "a") as f:
        f.write("This file is for a Hospital administrator\n")
    with open(filename, "a") as f:
        f.write("Date : {}".format(datetime) + "\n")
    # The user picks Option one if he is a new User and he wants to register his Company for the first time
    if InsuranceWork == 1:
        f.write("Email address : " + str(2) + "\n")


        print("Thanks for agreeing to work with us")
        InsuranceName = input("Kindly Input the name of the Insurance Company")
        with open(filename, "a") as f:
            f.write("Email address : " + InsuranceName + "\n")
        InsurancePolicy = input("Kindly input if your Insurance plan is monthly or Yearly")
        with open(filename, "a") as f:
            f.write("Email address : " + InsurancePolicy + "\n")
        InsuranceId = int(input("What is your ID Number"))
        with open(filename, "a") as f:
            f.write("Email address : " + str(InsuranceId) + "\n")
        Subscribers = []
        subscribers = input("The name of your first Subscriber on Your List")
        with open(filename, "a") as f:
            f.write("Email address : " + subscribers+ "\n")
        Subscriber1 = input("The name of the Second")
        with open(filename, "a") as f:
            f.write("Email address : " + Subscriber1 + "\n")
        Subscriber2 = input("Kindly enter the Third")
        with open(filename, "a") as f:
            f.write("Email address : " + Subscriber2 + "\n")
        Subscribers.append(subscribers)
        Subscribers.append(Subscriber1)
        Subscribers.append(Subscriber2)
        Insurance3 = Insurance(InsuranceName, InsurancePolicy, InsuranceId, Subscribers)
    # This Option is for already existing Customers  who want to add New Subscribers to his/her group
    elif InsuranceWork == 2:
        f.write("Email address : " + str(2) + "\n")

        Insurancename = input("Kindly enter your hospital name")
        f.write("Email address : " + Insurancename + "\n")

        Name = input("Kindly enter your name")
        f.write("Email address : " + Name + "\n")
        Age = input("Kindly enter your age")
        f.write("Email address : " + Age + "\n")
        Gender = input("Kindly enter your gender")
        f.write("Email address : " + Gender + "\n")
        print(Name, "You have been added to our Subscriber List")
        if Insurancename == "Policy":
            Insurance2List.append(Name)
        elif Insurancename == "Health Line":
            Insurance1List.append(Name)

    elif InsuranceWork == 3:
        f.write("Email address : " + str(2) + "\n")

        Name = input("Kindly input the name of your Hospital")

# If the user wants to log in as a private Doctor
elif Apply == 3:

    repeat_actions = True
    with open(filename, "a") as f:
        f.write("This file is for a Hospital administrator\n")
    with open(filename, "a") as f:
        f.write("Date : {}".format(datetime) + "\n")
    print("Welome to the private Sector of Our Hospital")
    Private = int(input("Enter 1 if you intend to register\n"
                        "Enter 2 if you intend to write articls"))
    # Option 1 for registering as a new member of Private Doctors
    if Private == 1:
        f.write("Email address : " + str(1) + "\n")
        name = input("Kindly input your name")
        with open(filename, "a") as f:
            f.write("Email address : " + name+ "\n")

        iD = str(input("Kindly input your ID"))
        with open(filename, "a") as f:
            f.write("Email address : " + iD+ "\n")
        Qualification = input("Kindly enter your area of Specialization")
        with open(filename, "a") as f:
            f.write("Email address : " + Qualification + "\n")
        Gender = input("Kindly enter your gender")
        with open(filename, "a") as f:
            f.write("Email address : " + Gender + "\n")
        Clinic = input("Kindly input the Clinic where you work")
        with open(filename, "a") as f:
            f.write("Email address : " + Clinic + "\n")
        Ratings = int(input("Kindly enter ratings"))
        with open(filename, "a") as f:
            f.write("Email address : " +str(Ratings) + "\n")
        Articles = input("List your articles")
        with open(filename, "a") as f:
            f.write("Email address : " + Articles + "\n")
        New_Doctor = PrivateDoctors(name, iD, Qualification, Gender, Clinic, Ratings, Articles)
        # This is for already existing Doctors Who wanna write articles
    elif Private == 2:
        f.write("Email address : " + str(2) + "\n")

        name = input('Kindly Input your name')
        f.write("Email address : " + name + "\n")
        Article = input("What is your article about")
        f.write("Email address : " + Article + "\n")
        article = input("Kindly input your articles")
        f.write("Email address : " + article + "\n")

elif Apply == 4:
    repeat_actions = True
    with open(filename, "a") as f:
        f.write("This file is for a Hospital administrator\n")
    with open(filename, "a") as f:
        f.write("Date : {}".format(datetime) + "\n")
    patient = int(input("Enter 1 if you want to register\n"
                        "Enter 2 if you want to view a list of Our hospital partners\n"
                        "Enter 3 if you want to view a list of our Private Doctors\n"
                        "Enter 4 if you want to view a list of our Insurance Companies\n"
                        "Enter 5 if you want to join a hospital\n"))

    if patient == 1:
        f.write("Email address : " + str(1) + "\n")

        New_Patient = input("Kindly input your name")
        f.write("Email address : " + New_Patient + "\n")

        age = int(input("kindly enter your age"))
        f.write("Email address : " +str (age) + "\n")
        gender = input("Kindly input your gender")
        f.write("Email address : " + gender + "\n")
        IdNmber = str(("Kindly input your ID Number on your passport"))
        f.write("Email address : " + IdNmber + "\n")
        Country = input("Kindly input your Nationality")
        f.write("Email address : " + Country + "\n")
        Occupation = input("Kindly input your Occupation")
        f.write("Email address : " + Occupation + "\n")
        Patient1 = PrivatePatients(New_Patient, age, gender, IdNmber, Country, Occupation)
    elif patient == 2:
        f.write("Email address : " + str(2) + "\n")

        for x in hospital:
            print(x)

    elif patient == 4:
        f.write("Email address : " + str(4) + "\n")

        for x in insurance:
            print(x)

    elif patient == 3:
        f.write("Email address : " + str(3) + "\n")

        print(doctor)

    elif patient == 5:
        f.write("Email address : " + str(5) + "\n")

        for x in hospital:
            print(x)
            print("Hospital Name:", Hospital3.Name)

            print("Those are the list of our hospitals")
            print(Hospital2.Services)
            print(Hospital3.Services)
            Input = int(input("Kindly enter the option you would like"))
            if Input == 1:
                print("You are being redirected to ICH's portal")
            elif Input == 2:
                print("You are being redirected to Redmond's portal")
