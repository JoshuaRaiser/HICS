import random
import math

from scipy.optimize import fsolve
from objects.ion import Ion

class Calculate:

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.w = 0                          # the parameter w of the 3pF and 3pG models
        self.po = 1                         # initial nuclear density
        self.p = random.uniform(0, 1)       # final nuclear density, random number (0 < p < 1)
        self.actual_ion = Ion()             # just the actual Ion type(objects/ion.py)
        self.F = 0.0

    '''
    ' @Calculate
    ' this functions calculate the nuclear density (r)
    ' entries -> Ion type(objects/ion.py)
    ' exit -> nuclear density (float)
    '''
    def calculate_nuclear_density(self, ion):
        self.F = random.uniform(0, 1)
        self.actual_ion = ion
        return fsolve(self.__calculate_find_root_integrated, 0.0)

    '''
    ' @Calculate
    ' this function calculate the x position of nucleon into the ion
    ' entries -> nd (nuclear density (float))
    ' exit -> x (float)
    '''
    def calculate_x(self, nd, o):
        return (nd * math.cos(o))

    '''
    ' @Calculate
    ' this function calculate the y position of nucleon into the ion
    ' entries -> nd (nuclear density (float))
    ' exit -> y (float)
    '''
    def calculate_y(self, nd, o):
        return (nd * math.sin(o))

    '''
    ' @Calculate
    ' this function calculate the X of function already integrated
    '
    '   Integrate
    '   / r
    '   |    (1 / (1 + e^((r - R) / a))) * dr , where r = x
    '   / 0
    '
    '   Integrated
    '   1 / R [ r - a * ln(e^(R/a) + e^(r/a)) + R] - F = 0,
    '   where F is a random number between 0 and 1: (0 < F < 1)
    '       
    ' entries -> x (float)
    ' exit -> next_x (float)
    '''
    def __calculate_find_root_integrated(self, x):
        ion = self.actual_ion
        next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - self.F
        return next_x

