class Ion:

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.symbol = ""        # the symbol of ion in the periodic table
        self.a = 0.0            # skin depth
        self.R = 0.0            # nuclear radius
        self.atom_num = 0      # atomic mass

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
    def define_atom_num(self, value):
        self.atom_num = value

    '''
    ' @Define
    ' this function define the symbol (name) of the ion in the periodic table
    ' entries -> value (string)
    '''
    def define_symbol(self, value):
        self.symbol = value

    '''
    ' @Define
    ' this function load the Gold Ion configuration
    '''
    def define_gold_ion(self):
        self.define_symbol("Au (atomic mass=197, atomic number=79)")
        self.define_a(0.535)
        self.define_r(6.38)
        self.define_atom_num(79)

    '''
    ' @Define
    ' this function load the Copper Ion configuration
    '''
    def define_copper_ion(self):
        self.define_symbol("Cu (atomic mass=63, atomic number=29)")
        self.define_a(0.5977)
        self.define_r(4.20641)
        self.define_atom_num(29)
