import random
import math

from scipy.optimize import fsolve
from objects.ion import Ion

class Calculate:

    RIGHT = 1
    LEFT = 0

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.w = 0                          # the parameter w of the 3pF and 3pG models
        self.po = 1                         # initial nuclear density
        self.p = random.uniform(0, 1)       # final nuclear density, random number (0 < p < 1)
        self.F = random.uniform(0, 1)       # a random number between 0 and 1 (0 < F < 1)
        self.actual_ion = Ion()             # just the actual Ion type(objects/ion.py)
        self.impact_param = 0.0             # parameter of the impact of the collision

    '''
    ' @Calculate
    ' this functions calculate the nuclear density (r)
    ' entries -> Ion type(objects/ion.py)
    ' exit -> nuclear density (float)
    '''
    def calculate_nuclear_density(self, ion):
        self.actual_ion = ion
        # Todo: don't use the ion radius to be impact parameter
        self.impact_param = 0.5 #self.actual_ion.R
        return fsolve(self.__calculate_find_root_integrated, 0.0)

    '''
    ' @Calculate
    ' this function calculate the x position of nucleon into the ion
    ' entries -> nd (nuclear density (float)), theta_angle (float)
    ' exit -> x (float)
    '''
    def calculate_x(self, nd, theta_angle, direction):
        if direction == Calculate.RIGHT:
            return ((nd * math.cos(theta_angle))) + self.impact_param / 2
        elif direction == Calculate.LEFT:
            return ((nd * math.cos(theta_angle))) - self.impact_param / 2
        else:
            raise ValueError("The value of direction must be 1 for RIGHT or 0 for LEFT. (calculator.py>calculate_x)")

    '''
    ' @Calculate
    ' this function calculate the y position of nucleon into the ion
    ' entries -> nd (nuclear density (float)), theta_angle (float)
    ' exit -> y (float)
    '''
    def calculate_y(self, nd, theta_angle):
        return (nd * math.sin(theta_angle))

    '''
    ' @Calculate
    ' this function calculate the X of function already integrated (when w is 0)
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
        # Todo: develop and integrate an equation to do a method when w is not 0
        ion = self.actual_ion
        next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - self.F
        return next_x
