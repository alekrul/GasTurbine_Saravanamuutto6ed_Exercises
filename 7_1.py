from math import *
import numpy as np

U = 360 #[m/s]
Va = 260 #[m/s]
alpha2 = radians(65)
alpha3 = radians(10)
m_dot = 20 #[kg/s]
T_01 = 1000 #[K]
p_01 = 4 #[bar]

#constant
cp = 1148
gamma = 1.333
aux = gamma/(gamma-1)
R = 0.287

tg_beta2 = tan(alpha2) - U/Va
tg_beta3 = tan(alpha3) + U/Va

reaction = (Va/(2*U))*(tg_beta3 - tg_beta2)
load_coeff = (2*Va/U)*(tg_beta2+tg_beta3)

work = m_dot*U*Va*(tg_beta2+tg_beta3)
print("Work: ", work)

V2 = Va/(cos(alpha2))

loss = 0.05

T_02 = T_01
T_2 = T_02 - (V2**2)/(2*cp)

T_2prime = T_2 - loss*(V2**2)/(2*cp)

p_2 = p_01/((T_02/T_2prime)**aux)

p_c = p_01/((gamma+1)/2)**aux #for M=1 throat

rho_2 = p_2*100/(R*T_2)

A_2 = m_dot/(rho_2*Va)

A_2a = A_2*cos(alpha2)
print(A_2a)