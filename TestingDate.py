class User:
    def __init__(self, firstn, lastn, age, phone_no, day, month, year):
        self.firstn = firstn
        self.lastn = lastn
        self.age = age
        self.phone_no = phone_no
        self.day = day
        self.month = month
        self.year = year

    def full_name(self):
        print(self.firstn + " " + self.lastn)

    def dob(self):
        print(self.day + "/" + self.month + "/" + self.year)

    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "And their date of birth is " + f"{self.day}" + "/" + f"{self.month}" + "/" + f"{self.year}"
        return_string += "--------------------------------------\n"
        return return_string

User_name = input("What is your name? ")
print("Welcome to " + User_name + "'s Contact Book")
print("Please enter the contact's information")
first_name = input("First Name = ")
last_name = input("Last Name = ")
while True:
    try:
        age=int(input("Age = "))
        break
    except:
        print("only integers allowed, please re-enter a number")
        print("Thank you")
while True:
    try:
        phone_number=int(input("Phone Number = "))
        break
    except:
        print("only integers allowed, please re-enter a number")
        print("Thank you")
# Working on this part of the code to ensure a dd/mm/yyyy sequence

while True:
    try:
        day=int(input("dd = "))
        if day not in range(1,31):
         break
    except:
        print("please enter your birthday in the format dd/mm/yyyy")
        print("Thank you")

while True:
    try:
        month=int(input("mm = "))
        if day not in range(1,12):
    break
    except:
        print("please enter your birthday in the format dd/mm/yyyy")
        print("Thank you")

while True:
    try:
        year=int(input("yyyy = "))
        break
    except:
        print("please enter your birthday in the format dd/mm/yyyy")
        print("Thank you")


dob = input("Their date of birth = ")



print("Thank You")

the_contact = User(first_name, last_name, age, phone_number, dob, day, month, year)
print(the_contact)

