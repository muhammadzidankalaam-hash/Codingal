# create class
class IOString():

	# constructor to set default value
    def __init__(self):
        self.str1 = ""

	# function to get input from user
    def get_String(self):
        self.str1 = input("Enter String : ")

	# function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()
