import random
import math

class Calculate:

    #
    # @Constructor
    # this is the constructor method for this class
    #
    def __init__(self):
        self.w = 0                          # the parameter w of the 3pF and 3pG models
        self.po = 1                         # initial nuclear density
        self.p = random.uniform(0, 1)       # final nuclear density

    #
    # @Calculate
    # this functions calculate the nuclear density (r)
    # entries -> Ion (objects/ion.py)
    # exit -> nuclear density (float)
    #
    def calculate_nuclear_density(self, ion):
        return (ion.a * (math.log(math.fabs(self.p/self.po - 1))) + ion.R)

    #
    # @Calculate
    # this function calculate the x position of nucleon into the ion
    # entries -> nd (nuclear density (float))
    # exit -> x (float)
    #
    def calculate_x(self, nd):
        o = random.randint(0, 360)
        return (nd * math.cos(o))

    #
    # @Calculate
    # this function calculate the y position of nucleon into the ion
    # entries -> nd (nuclear density (float))
    # exit -> y (float)
    #
    def calculate_y(self, nd):
        o = random.randint(0, 360)
        return (nd * math.sen(o))
