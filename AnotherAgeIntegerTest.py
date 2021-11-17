class User:
    def __init__(self, firstn, lastn, age, phone_no, dob):
        self.firstn = firstn
        self.lastn = lastn
        self.age = age
        self.phone_no = phone_no
        self.dob = dob
    def checking_integer_inputs(input):
        try:
            # Trying to test whether the input was or wasn't an integer
            val = int(input)
        except ValueError:
                #This except rule prevents strings and floats from being an input giving us clean whole integers in the age and phone number section of the code
                print("This is not a valid input for this request, please try again")
    def full_name(self):
        print(self.firstn + " " + self.lastn)
    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "And their date of birth is " +f"{self.dob}\n"
        return_string += "--------------------------------------\n"
        return return_string
User_name = input("What is your name? ")
print("Welcome to " + User_name + "'s Contact Book")
print("Please enter the contact's information")
first_name = input("First Name = ")
last_name = input("Last Name = ")


# Testing this part of the code
# Trying to create a loop to ensure that the age can only be submitted as an integer
while True:
    try:
        age = int(input("Age = "))
        break
    except ValueError:
        print("Please input an integer") 
        continue
# Confirmed, does not do as intended

phone_number = input("Phone Number = ")
dob = input("Date of Birth (dd/mm/yyyy) = ")