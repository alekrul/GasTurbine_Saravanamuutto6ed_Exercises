from math import *
import numpy as np

pr = 10
eta_centrifugal_poly = 0.83
eta_axial_poly = 0.92

#axial compressor
deltaT0_s = 30 #[K]
alpha1 = radians(20)
alpha3 = alpha1
d_mean = 0.25 #[m]
T_01 = 288 #[K]
p_01 = 1.01 #[bar]
work_done_factor = 0.86
Va = 150 #[m/s]

#centrifugal compressor
d_tip = 0.33 #[m]
slip = 0.9
power_input_factor = 1.04

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#starting with the axial compressor
from sympy import symbols, Eq, solve

U, tg_beta1 = symbols('U tg_beta1')

#reaction 0.5 at mean:

b1 = Va*tan(alpha1)
b2 = deltaT0_s*cp/(work_done_factor*Va)

eq1 = Eq(U - Va*tg_beta1,b1)
eq2 = Eq(U*tg_beta1 - U*tan(alpha1),b2)


solutions = solve((eq1, eq2), (U, tg_beta1))

U = [value[0] for value in solutions if value[0] > 0]
tg_beta1 = [value[1] for value in solutions if value[1] > 0]

N = U[0]/(pi*d_mean)

print(N)

#for the centrifugal compressor
#we need conditions at cent. compressor inlet
exp_poly = (1/eta_axial_poly)*(1/aux)

T_02 = T_01 + deltaT0_s*4
p_03 = p_01*((T_02/T_01)**(1/exp_poly))

p_01_c = p_03
T_01_c = T_02

p_03_c = p_01*pr

pr_c = p_03_c/p_01_c
eta_iso_c = (pr_c**aux -1)/(pr_c**(1/exp_poly) -1)

U = sqrt((pr_c**(1/aux)-1)*cp*T_01_c/(eta_iso_c*power_input_factor*slip))


N = U/(pi*d_mean)

print(N)