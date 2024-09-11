from math import *
import numpy as np

T_01 = 1050 #[K]
p_01 = 3.8 #[bar]
pr = 2
V3 = 275 #[m/s]
Ur = 300 #[m/s]
eta_t = 0.88
reaction_r = 0
V1 = V3
tip_root_ratio = 1.4
nozzle_loss = 0.05

#constant
cp = 1148
gamma = 1.333
aux = gamma/(gamma-1)
R = 0.287

#calculate nozzle efflux angle alpha2 and blade inlet angles beta2 at root
#nozzle efflux angle and degree of reaction at tip
#static pressure at inlet and outlet of rotor blades at root

deltaT = eta_t*T_01*(1 - ((1/pr)**(1/aux)))
T_03 = T_01 - deltaT

V2u = cp*deltaT/Ur

#as reaction=0 at root, T2 = T3
T_02 = T_01
T_3 = T_03 - (V3**2)/(2*cp)
print(T_3)
V2 = sqrt(2*cp*(T_02-T_3))

alpha2 = asin(V2u/V2)
print("Alpha 2 at root: ", degrees(alpha2))

Va = sqrt(V2**2 - V2u**2)

beta2 = atan((V2u - Ur)/Va)

print("Beta 2 at root: ", degrees(beta2))

#considering free vortex design
V2u_t = V2u/tip_root_ratio

alpha2_t = atan(V2u_t/Va)
print("Alpha 2 at tip: ", degrees(alpha2_t))
V2_t = sqrt(V2u_t**2 + Va**2)

T_2_tip = T_02 - (V2_t**2)/(2*cp)
reaction_tip = (T_2_tip-T_3)/deltaT

print("Reaction at tip: ", reaction_tip)

T_2_loss = T_02 - (1+nozzle_loss)*(V2**2)/(2*cp)

p_2 = p_01/((T_01/T_2_loss)**aux)
p_3 = (p_01/pr)/((T_03/T_3)**aux)

print("Static pressure 2: ", p_2)
print("Static pressure 3: ", p_3)