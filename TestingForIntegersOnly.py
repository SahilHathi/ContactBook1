class User:
    def __init__(self, firstn, lastn, age, phone_no):
        self.firstn = firstn
        self.lastn = lastn
        self.age = age
        self.phone_no = phone_no

    def full_name(self):
        print(self.firstn + " " + self.lastn)
 
    def __str__(self):
        return_string = "--------------------------------------\n"
        return_string += "The contact's name is" + " " + f"{self.firstn} {self.lastn}\n"
        return_string += "Their age is " + f"{self.age}\n"
        return_string += "And their phone number is " +f"{self.phone_no}\n"
        return_string += "--------------------------------------\n"
        return return_string
    

print("Please Insert a Number:")

def getNumberInput():
        global value
        value = input()
        while not value.isnumeric():
            print("Enter a number ")
            value = input("Enter again ")
        return int(value)

getNumberInput()
print(value)
