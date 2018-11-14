# house.py
#   This program creates a house of a picture by only getting five clicks from the user.
#   A program by Sergio Sum
#   3/13/17

from graphics import *

def main():
    # Making the window for the user to build the house
    win = GraphWin("House", 750, 750)
    win.setCoords(-500, -500, 500, 500)
    win.setBackground("gray")

    # getting the points from the user for frame of the house
    directions = Text(Point(0, -480), "The first two clicks will draw the frame of our house. 1st click = bottom left and 2nd click = top right corner").draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    # using points to draw the frame
    frame = Rectangle(p1, p2)
    frame.setFill("cyan")
    frame.draw(win)

    # instruction for door
    directions.setText("Thanks honey. Now, the third click will be the center of the top edge of the door.")
    p3 = win.getMouse()
    p3.draw(win)
    # setting the width of the door
    doorWidth = (p2.getX() - p1.getX())/5
    # setting the opposite corners to draw the rectangle using the width of the door
    doorTopLeft = Point(p3.getX() - doorWidth/2, p3.getY())
    doorBottomRight = Point(p3.getX() + doorWidth/2, p1.getY())
    door = Rectangle(doorTopLeft, doorBottomRight)
    door.setFill("lightsalmon")
    door.draw(win)

    # instruction for window
    directions.setText("Sweet. The fourth click will draw the window of our house house.")
    p4 = win.getMouse()
    # setting the width of the window
    windowWidth = doorWidth/2
    # setting the opposite corners to draw the square using the width of the door
    windowBL = Point(p4.getX()- windowWidth/2, p4.getY() - windowWidth/2)
    windowTR = Point(p4.getX() + windowWidth/2, p4.getY() + windowWidth/2)
    window = Rectangle(windowBL, windowTR)
    window.setFill("white")
    window.draw(win)

    # instruction for roof
    directions.setText("Great! The fifth click will be the top point of the roof. You're almost there!")
    p5 = win.getMouse()
    p5.draw(win)
    # finding the missing point to make the triangle
    missingTriPt = Point(p1.getX(), p2.getY())
    # Using polygon object to draw triangle
    roof = Polygon(p5, p2, missingTriPt)
    roof.setFill("cornsilk")
    roof.draw(win)
    # requiring click to leave window
    directions.setText("Thanks for building our house. HAPPY BIRTHDAY! I LOVE YOU")
    win.getMouse()
    win.close()
main()
    
    
