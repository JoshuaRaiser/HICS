import matplotlib.pyplot as plt
import random
import math

from objects.ion import Ion
from mathematics.calculator import Calculate

ouro = Ion()
ouro.define_a(0.535)
ouro.define_r(6.38)
ouro.define_atomic_mass(197)

plt.figure(1)

for index in range(ouro.atomMass):
    cal = Calculate()
    nd = cal.calculate_nuclear_density(ouro)[0]
    print("r: " + str(nd))
    print("F: " + str(cal.F))
    o = random.uniform(0, 2 * math.pi)
    x = cal.calculate_x(nd, o)
    y = cal.calculate_y(nd, o)
    plt.subplot(121)
    plt.title("nuclear density")
    plt.plot(x, y, '.b')
    plt.subplot(122)
    plt.title("x= r y= P(r)/P(0)")
    plt.plot(nd, (cal.po*(1+cal.w*((nd/ouro.R)**2))/(1+math.exp((nd-ouro.R)/ouro.a))/cal.po), '.k')
    print("X " + str(x) + "\tY: " + str(y) + "\tr: " + str(nd))

plt.show()

