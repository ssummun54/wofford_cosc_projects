# COSC 235 - Assignment 1
# greet.py
# This assignment will ask for the user's full name and print it. It will also ask for the his/her age and wish the user a happy birthday the same amount of times as his/her's age. 
# A program by Sergio Sum. Written on 2/17/17

def main():
# Show title message
    print('COSC 235 - Assignment 1')
    print('Version 1.0')
    print()

# This asks for their names
    firstName = input("What is your first name? ")
    lastName = input("Thank you. Now, please enter your last name: ")

# This line will greet the user according to his/her input
    print("Greetings,", firstName, lastName + "!")


    age = eval(input("How old are you?"))
    
# I will tell them happy birthday the same amount of times as their age. 
    for i in range (age):
        print("Happy birthday!")
    

main()
