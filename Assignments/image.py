# image.py
# 4/29/17
#   This program applies a filter to a picture and then saves it as another file.
#   A program by Sergio Sum


#importing graphics
from graphics import *




def main():
    # getting name of file and adding .gif
    fileName = input("Please enter the name of an image file: ") + ".gif"

    #setting up graph and loading picture 
    win = GraphWin("Picture", 400, 400)
    win.setBackground("gray")

    image = Image(Point(200,200), fileName)
    image.draw(win)

    # finding amount of rows and columns
    columns = image.getWidth()
    rows = image.getHeight()

    # converting to grayscale
    print("Converting your image to grayscale...")
    for y in range (rows):
        for x in range (columns):
            r, g, b, = image.getPixel(x, y)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(x, y, color_rgb(brightness, brightness, brightness))
        update()
    print("Saving your grayscale image...")
    image.save(fileName[0:-4] + "_grayscale.gif")
    win.close()

    # converting to negative 
    print("Converting your image to negative...")
    win2 = GraphWin("Picture", 400, 400)
    win2.setBackground("gray")
    image2 = Image(Point(200,200), fileName)
    image2.draw(win2)

    for y in range (rows):
        for x in range (columns):
            r, g, b, = image2.getPixel(x, y)
            image2.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))
        update()
    #print("Saving your negative image...")
    #image2.save(fileName[0:-4] + "_negative.gif")     getting too many colors error
    win2.close()

    print("Finished!")

main()
