# sphere.py
#   This program contains the sphere class.
#   A program by Sergio Sum
#   5/5/17

from math import *

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return 4/3 * pi* self.radius **3
