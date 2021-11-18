class User:
    def __init__(self, firstn, lastn, age, phone_no, dob):
        self.firstn = firstn
        self.lastn = lastn
        self.age = age
        self.phone_no = phone_no
        self.dob = dob
    def checking_integer_inputs(input):
        try:
            val = int(input)
        except ValueError:
                print("This is not a valid input for this request, please try again")
    def full_name(self):
        print(self.firstn + " " + self.lastn)
    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "And their date of birth is " + f"{self.dob}\n"
        return_string += "--------------------------------------"
        return return_string

contacts = list()
users_input = ""
User_name = input("What is your name? ")
print("Welcome to " + User_name + "'s Contact Book")
# Using list, now the code will display options in a while loop for the user to use;

while users_input != "e":
    print("Please select one of these options:")
    print("1 - Input a contact")
    print("2- Display contacts")
    print("e - Exit terminal")
    users_input = input("Select option: ")

    if users_input == "1":
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
                print("Only integers allowed, please re-enter a number")
                print("Thank you")

        dob = input("Their date of birth = ")

        the_contact = User(first_name, last_name, age, phone_number, dob)
        # this stores the contact data
        contacts.append(the_contact)
        print("Thank you")
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("All contacts have now been displayed. Press Enter to continue")
        #the .lower allows the user to input a capital E and the string method to still work. QoL change
    elif users_input.lower() == "e":
        break


print("Thank you for using this application!")

