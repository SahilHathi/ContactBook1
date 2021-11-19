#importing os to help work with files, ie: to create a csv file if it's missing
import os

# Creating a class to structure the data better
class User:
    def __init__(self, firstn, lastn, age, phone_no, dob):
        self.firstn = firstn
        self.lastn = lastn
        self.age = age
        self.phone_no = phone_no
        self.dob = dob

    def full_name(self):
        return f'{self.firstn} {self.lastn}'
        
# Creating a format for the user

    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "And their date of birth is " + f"{self.dob}\n"
        return_string += "--------------------------------------"
        return return_string

contacts = list()

# List data structure creates an empty section of memory that can be edit stuff onto it
# If statement to see whether or not the file is in the system, if not it will create one

# This is used to save the data from previous inputs. If the file isn't there then that means that the data has
# been deleted, if it is there then it'll use what is already on the file.

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:

# This will automatically read the lines

        f_list = f.readlines()
        for f_line in f_list:

# The .rstrip removes the \n at the end and the .split will removes the commas.

            contact_data = f_line.rstrip()
            contact_data = f_line.split(",", ".")
            contact = User(contact_data[0], contact_data[1], contact_data[2], contact_data[3], contact_data[4],)
            contacts.append(contact)

users_input = ""


User_name = input("What is your name? ")

print("Welcome to " + User_name + "'s Contact Book")

# Using list, now the code will display options in a while loop for the user to use;

while users_input != "e":
    print("Please select one of these options:")
    print("1 - Input a contact")
    print("2 - Display contacts")
    print("3 - Search for a contact")
    print("e - Exit terminal")
    users_input = input("Select option: ")

# Create a conditional check

    if users_input == "1":
        print("Please enter the contact's information")

# This will be user input
# There will be specific data types for each one, ages should be number integers as well as phonenumbers,
# preventing any type of non-numerical inputs

        first_name = input("First Name = ")
        last_name = input("Last Name = ")

# Finally created a way to only get integer inputs, there should be a way easier to use this for both age and phone
# number so that I don't have to type it twice but this will be a placeholder at least since it works as intended.

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
                print("Only integers allowed, please re-enter a number")
                print("Thank you")

        dob = input("Their date of birth (dd/mm/yyyy) = ")

        the_contact = User(first_name, last_name, age, phone_number, dob)

# This stores the contact data
  
        contacts.append(the_contact)
        print("Thank you")
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("All contacts have now been displayed. Please press the Enter key to continue")

# The .lower function allows the iser to input a capital 'e' "(E)" and the string method would still accept it as the
# exit function. Just a small quality of life feature.

    elif users_input == "3":
        search = input("Enter a contact's name to search for\n")
        for contact in contacts:
            if search in contact.full_name():
                print(contact)

            
    elif users_input.lower() == "e":
        break

# If the file doesn't exist this should handle that gap of information

with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(f'{contact.firstn}, {contact.lastn}, {contact.age}, {contact.phone_no}, {contact.dob}\n')


print("Thank you for using this application")