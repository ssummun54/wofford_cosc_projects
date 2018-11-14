# archery.py
# This program tells you your score in archery
# Sergio Sum
# 4/22/17

#import graphics
from graphics import *
#import math
from math import *

#function that computes score
def computeScore(x2,y2):
    x1 = 0
    y1 = 0
    #points for distance formula and then executing the formula based on x and y from clicks
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    # deciding the score to return to main
    if distance <= 1:
        return 9
    elif distance <= 2:
        return 7
    elif distance <= 3:
        return 5
    elif distance <= 4:
        return 3
    else:
        return 1
    
def main():
    # Create a window
    win = GraphWin("Archery Target", 400, 400)
    win.setCoords(-6, -6, 6, 6)
    win.setBackground("gray")
    center = Point(0,0)

    c1 = Circle(center, 5)
    c1.setFill("white")
    c1.draw(win)

    c2 = Circle(center, 4)
    c2.setFill("black")
    c2.draw(win)

    c3 = Circle(center, 3)
    c3.setFill("blue")
    c3.draw(win)

    c4 = Circle(center, 2)
    c4.setFill("red")
    c4.draw(win)

    c5 = Circle(center, 1)
    c5.setFill("yellow")
    c5.draw(win)

    # placeholder
    score = 0

    # text for score, score variable will update since score was made into a string
    currentScore = Text(Point(0, - 5.5), "Your current score is: "+ str(score))
    currentScore.draw(win)


    # loop for 5 clicks, drawing clicks, and getting the score by calling currentScore,
    #    and updating score variable
    for clicks in range (1,6):
        clicks = win.getMouse()
        clicks.setFill("cyan")
        clicks.draw(win)
        score += computeScore(clicks.getX(), clicks.getY())
        currentScore.setText("Your current score is:"+str(score))

    currentScore.setText("Your final score is: " + str(score)+". Click to leave")

    win.getMouse()
    win.close()


main()
