# imports
import math
import random

# imports from
from objects.ion import Ion

# error messages
ERROR_INVALID_DIRECTION_MESSAGE = 'Invalid direction error.'

# directions
RIGHT = 0
LEFT = 1

# constants vars
a_em = 1/137
proton_radius = 0.84    # 0.84 - 0.87
# Todo: 200 or 200000? Fabs to avoid negative number root square? Ask to Marcelo.
vn = math.sqrt(math.fabs(1 - (2*938.272046)/math.sqrt(200)))

def main():

    # vars list
    impact_parameter = 0.0
    impact_parameter_limit = 12
    for_count = 100

    # electromagnetic field event results
    eEx_event = []
    eEy_event = []
    eBx_event = []
    eBy_event = []

    while impact_parameter <= impact_parameter_limit:

        for index in range(for_count):
            # ions in collision
            ion = Ion()
            ion.define_gold_ion()

            nucleons_positions_xy_right_ion = initialize_nucleons_list(ion, RIGHT, impact_parameter)
            nucleons_positions_xy_left_ion = initialize_nucleons_list(ion, LEFT, impact_parameter)

            # calculate the electric field
            eExy_right = electric_field(nucleons_positions_xy_right_ion)
            eExy_left = electric_field(nucleons_positions_xy_left_ion)

            # calculate the magnetic field
            eBxy_right = magnetic_field(nucleons_positions_xy_right_ion, RIGHT)
            eBxy_left = magnetic_field(nucleons_positions_xy_right_ion, RIGHT)

            # calculate the events and add to the respective event list
            eEx_event.append(eExy_right[0] + eExy_left[0])
            eEy_event.append(eExy_right[1] + eExy_left[1])
            eBx_event.append(eBxy_right[0] + eBxy_left[0])
            eBy_event.append(eBxy_right[1] + eBxy_left[1])

        impact_parameter += 2


def initialize_nucleons_list(ion, direction, impact_param):
    xy_nucleons_list = []
    pos_x = 0
    pos_y = 0

    for index in range(ion.atom_num):
        r = random.uniform(0, ion.R)
        theta_angle = random.uniform(0, 2*math.pi)

        if direction == RIGHT:
            pos_x = r * math.cos(theta_angle) + impact_param/2

        elif direction == LEFT:
            pos_x = r * math.cos(theta_angle) - impact_param/2

        else:
            raise ValueError(ERROR_INVALID_DIRECTION_MESSAGE)

        pos_y = r * math.sin(theta_angle)
        xy_nucleons_list.append([pos_x, pos_y])

    return xy_nucleons_list

def electric_field(nucleon_list):
    e_x, e_y = 0, 0
    sum_x, sum_y = 0, 0
    for index in range(len(nucleon_list)):
        x = nucleon_list[index][0], y = nucleon_list[index][1]

        # Todo: really need do this verification yet? Ask to Marcelo.
        if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
            rn = math.sqrt(x ** 2 + y ** 2)
            sum_x += -x / (rn ** 3)
            sum_y += -y / (rn ** 3)

    e_x = a_em / math.sqrt(1 - (vn ** 2)) * sum_x
    e_y = a_em / math.sqrt(1 - (vn ** 2)) * sum_y
    return [e_x, e_y]

def magnetic_field(nucleon_list, direction):
    e_x, e_y = 0, 0
    sum_x, sum_y = 0, 0
    if direction == RIGHT:
        for index in range(len(nucleon_list)):
            x = nucleon_list[index][0], y = nucleon_list[index][1]

            # Todo: really need do this verification yet? Ask to Marcelo.
            if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
                rn = math.sqrt(x ** 2 + y ** 2)
                sum_x += -x / (rn ** 3)
                sum_y += y / (rn ** 3)

        e_x = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_x
        e_y = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_y
        return [e_x, e_y]

    elif direction == LEFT:
        for index in range(len(nucleon_list)):
            x = nucleon_list[index][0], y = nucleon_list[index][1]

            # Todo: really need do this verification yet? Ask to Marcelo.
            if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
                rn = math.sqrt(x ** 2 + y ** 2)
                sum_x += x / (rn ** 3)
                sum_y += -y / (rn ** 3)

        e_x = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_x
        e_y = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_y
        return [e_x, e_y]

    else:
        raise ValueError(ERROR_INVALID_DIRECTION_MESSAGE)

if __name__ == "__main__":
    main()
