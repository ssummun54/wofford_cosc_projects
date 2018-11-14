# invest.py
#   This program evaluates a user's investment by investing the innitial amount each year.
#   A program by Sergio Sum
#   2/24/17


def main():
    
    # display a description of the program
    print("This program calculates your ending balance when you choose an amount to invest for a certain amount of years.")

    print()

    # obtain amount of money to be invested each year by user
    principle = float(input("How much money would you like to invest each year? $"))

    print()

    # obtain amount of years the user will invest the money
    years = eval(input("Thank you. How many years do you want to invest this amount? "))

    print()

    # obtain interest rate on investment
    apr = eval(input("Okay. Enter the annual interest rate on your investment: "))

    print()

    # place holder variable where the balance at the end of each year will be collected
    investment = 0
    
    # making a loop that starts at year 1 and stops at the exact year the user said
    for investmentAmount in range (1, years + 1):

       #formula to calculate balance each year and add the principle amount each year
        balance = (investment + principle) * (1 + apr/100)

        # using the temporary variable to hold the new balance
        investment = balance 

        # displaying results
        print("In year", investmentAmount, "at APR", apr/100, "your balance will be", round(balance, 2), "dollars.")
        print()

    #displaying final result
    print("Your total balace will be", round(balance, 2), "dollars after", years, "years.") 

main()
              
        
    
    
