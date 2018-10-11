class Ion:

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.symbol = ""        # the symbol of ion in the periodic table
        self.a = 0.0            # skin depth
        self.R = 0.0            # nuclear radius
        self.atom_num = 0       # atomic mass
        self.gev = 0            # energy at collision

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
    ' this function define the energy used in the collision
    ' entries -> value (float)
    '''
    def define_gev(self, value):
        self.gev = value

    '''
    ' @Define
    ' this function load the Gold Ion configuration
    '''
    def define_gold_ion(self):
        self.define_symbol("Au (atomic mass=197, atomic number=79)")
        self.define_a(0.535)
        self.define_r(6.38)
        self.define_atom_num(79)
        self.define_gev(200)

    '''
    ' @Define
    ' this function load the Lead Ion configuration
    '''
    def define_lead_ion(self):
        self.define_symbol("Pb (atomic mass=206, atomic number=82)")
        self.define_a(0.545)
        self.define_r(6.61)
        self.define_atom_num(82)
        self.define_gev(2760)
