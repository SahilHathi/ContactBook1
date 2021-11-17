# Creating a class to structure the data better
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

        # Creating a format for the user

    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "And their date of birth is " + f"{self.dob}\n"
        return_string += "--------------------------------------\n"
        return return_string


User_name = input("What is your name? ")

print("Welcome to " + User_name + "'s Contact Book")

print("Please enter the contact's information")

# This will be user input
# There will be specific data types for each one, ages should be number integers as well as phonenumbers, preventing any type of non-numerical inputs

first_name = input("First Name = ")
last_name = input("Last Name = ")

# Finally created a way to only get integer inputs, there should be a way easier to use this for both age and phone number so that I don't have to type it twice but this will be a placeholder at least since it works as intended.

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

dob = input("Their date of birth = ")



print("Thank You")

the_contact = User(first_name, last_name, age, phone_number, dob)
print(the_contact)

