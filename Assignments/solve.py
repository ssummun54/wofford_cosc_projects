# solve.py
#   This program contains the sphere class.
#   A program by Sergio Sum
#   5/5/17


# import sphere
from sphere import *

def main():
    #get radius
    radius = eval(input("Please enter a radius: "))

    #make sphere
    sphere = Sphere(radius)

    #results
    print("The surface area is ", sphere.surfaceArea())
    print("The volume is ", sphere.volume())

main()
