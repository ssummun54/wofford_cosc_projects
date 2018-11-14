# numerology.py
#   This program sums up the Unicode values of the user's full name and displays the corresponding Unicode character
#   A program by Sergio Sum
#   3/24/17

def main():
    name = input("Please enter your full name: ")
    # not counting spaces by turning to list
    name = name.split()
    #joining list
    name = "".join(name)

    # accumulator
    counter = 0

    # getting unicode values for for values in name:
        counter = counter + ord(values)
    print("Your value is:", counter)
    print("The Unicode character for your value is:", chr(counter))
main()
        
