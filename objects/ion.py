class Ion:

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.a = 0.0            # skin depth
        self.R = 0.0            # nuclear radius
        self.atomMass = 0       # atomic mass

    '''
    ' @Define
    ' this function define the a value
    ' entries -> value (float)
    '''
    def define_a(self, value):
        self.a = value

    '''
    ' @Define
    ' this function define the R value
    ' entries -> value (float)
    '''
    def define_r(self, value):
        self.R = value

    '''
    ' @Define
    ' this function define the atomMass value
    ' entries -> value (integer)
    '''
    def define_atomic_mass(self, value):
        self.atomMass = value

    '''
    ' @Define
    ' this function define the value of X and Y to the graph
    ' entries -> value[x (float), y (float)]
    '''
    def define_xy(self, value):
        self.xy = [value[0], value[1]]

    '''
    ' @Define
    ' this function load the Gold Ion configuration
    '''
    def define_gold_ion(self):
        self.define_a(0.535)
        self.define_r(6.38)
        self.define_atomic_mass(197)
