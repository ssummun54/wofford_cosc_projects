# pi.py
#   This program approximates pi by the series 4/1 - 4/3 + 4/5... However, the amount of times we go through the seires is determined by the user.
#   We will display the absolute and relative errors of the seires according with the number the user inputs.

#we are importing math to use math.pi, which is the actual result of pi
import math

def main():
    #description of program to user
    print("This program approximates the value of pi by using a series.")
    print("The amount of terms we use in the series depends on the integer you input.")
    print()
    
    #asking for input from user to show how many expressions in the series we want to go to
    n = int(input("Please enter a number greater than or euqal to 0: "))
    #accumulator
    approxPi = 0


    #loop to find the approximation of pi with the number the user input
    multiplier = 1
    for denominator in range (1, n * 2, 2):

        #formula
        approxPi = approxPi + 4/denominator * multiplier
        multiplier = multiplier * -1

    #displaying results
    print("The approximated value of pi is : ", approxPi)
    print("The actual value of pi is: ", math.pi)

    #setting variables to fine the errors
    absoluteError = abs(approxPi - math.pi)
    relativeError = absoluteError / abs(math.pi)

    #displaying result
    print("The absolute error is:", absoluteError)
    print("The relative error is:", relativeError, "which is", round(relativeError * 100, 3), "%")
          
    


            
            
            
    







main()
            
    
