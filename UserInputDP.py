# Task 1 Input Length Validator: Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def name_length():
    first_name = len(input("Please enter your first name: "))
    last_name = len(input("Please enter your last name: "))

    if first_name <= 2:
        print("Error: Name must be at least 2 characters long")

    if last_name <= 2:
        print("Error: Name must be at least 2 characters long")
    
    if first_name > 2 and last_name > 2:
        print("The input is valid")

name_length()