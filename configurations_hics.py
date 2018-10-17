'''
'     __ __                     ____            _____     _____    __          _____            __     __
'    / // /__ ___ __  ____ __  /  _/__  ___    / ___/__  / / (_)__/ /__ ____  / __(_)_ _  __ __/ /__ _/ /____  ____
'   / _  / -_) _ `/ |/ / // / _/ // _ \/ _ \  / /__/ _ \/ / / / _  / -_) __/ _\ \/ /  ' \/ // / / _ `/ __/ _ \/ __/
'  /_//_/\__/\_,_/|___/\_, / /___/\___/_//_/  \___/\___/_/_/_/\_,_/\__/_/   /___/_/_/_/_/\_,_/_/\_,_/\__/\___/_/
'                     /___/
'                         ___ ___  _  _ ___ ___ ___ _   _ ___    _ _____ ___ ___  _  _ ___
'                        / __/ _ \| \| | __|_ _/ __| | | | _ \  /_\_   _|_ _/ _ \| \| / __|
'                       | (_| (_) | .` | _| | | (_ | |_| |   / / _ \| |  | | (_) | .` \__ \
'                        \___\___/|_|\_|_| |___\___|\___/|_|_\/_/ \_\_| |___\___/|_|\_|___/
'
' This file contains all the configurable variables to the HICS - Heavy Ion Collider Simulator
'
' HICS is an Academic Work for obtains the Bachelor title in Computer Science
' Autor: Joshua Benjamin Raiser Tallmann, contact to: joshua_raiser@hotmail.com
'''

from objects.ion import Ion

'''
' These vars are directly involved in the collision simulation: 
'
'  # config_for_count -> means the number of times the simulation takes place by impact parameter range
'
'  # config_impact_parameter -> means the initial impact parameter of the collision
'
'  # config_impact_parameter_limit -> means the maximum impact parameter
'
'  # config_impact_parameter_interval -> means the interval in which the impact parameter will jump
'
'  # config_ion_type -> means the ion type used in the collision
'                       - There are two types of ions in the configurations:
'                           * gold (Au, 197, 79)
'                           * lead (Pb, 206, 82)
'''
                                            # Autor' considerations:
config_for_count = 1000                     # 1000 is a good choice the simulations
config_impact_parameter = 0                 # start in 0 to get a centralized collision
config_impact_parameter_limit = 14          # 14 is a good choice tho
config_impact_parameter_interval = 2        # 2 for the interval jump is good, never can't be 0!

config_ion_type = Ion()
config_ion_type.define_gold_ion()           # gold is nice to initial collisions simulations, later can try with others
