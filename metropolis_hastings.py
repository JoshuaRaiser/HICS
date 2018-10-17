import math
import random
from scipy.optimize import fsolve
from objects.ion import Ion

ion = Ion()

def main():
    ion.define_gold_ion()
    # Todo: perguntar ao Marcelo se é para considerar o valor de incidência dentro de um intervalo. Se sim, como fazer?
    # Todo: números próximos de zero, exemplo: 8.128917419e-08, ao arredondar o número passa a ser zero.
    for index in range(10000):
        r = fsolve(__calculate_find_root_integrated, 0.0)[0]
        print(r)

def __calculate_find_root_integrated(x):
    F = random.uniform(0, 1)
    next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - F
    return next_x

if __name__ == "__main__":
    main()