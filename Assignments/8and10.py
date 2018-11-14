# 8and10.py
#   This progam runs two functions. The first function uss Newton's Method to find the
#   square root of a number. The second function creates an acronym based on the phrase
#   given by the user. 

#importing math for square root
from math import *

#function for problem 8
def nextGuess(guess, newton): #(this is from runProblem8(someNumber, times)
    #starts guess
    estimate = guess/2
    # looping for starting with one and ending with the actual number the user input
    for i in range (1, newton + 1):
        estimate = (estimate + (guess / estimate))/2

    return estimate 

#function for problem 10
def acronym(phrase):
    #splitting phrase
    phrase = phrase.split()
    #new string where the letters will concactenate
    newString = ""
    for firstLetter in phrase:
        newString = newString + firstLetter[0].upper()
    return newString
        





   
#calls for problem 8 work
def runProblem8():
    #inputs
    someNumber = eval(input("Please enter a number: "))
    times = eval(input("How many times do you wish to run Newton's Method? "))
    #difference
    difference = round(float(sqrt(someNumber)) - round(nextGuess(someNumber, times), 10),14)
    #results
    print("The estimated square root of", someNumber, "is", round(nextGuess(someNumber, times), 10), "which has an error of", float(abs(difference)))

def runProblem10():
    phrase = input("Please enter a phrase: ")
    print("The acronym for your phrase is", acronym(phrase))

def main():
    print("Running Program 1 (Problem 8)...")
    runProblem8()
    print("Running Program 2(Problem 10)...")
    runProblem10()















main()
