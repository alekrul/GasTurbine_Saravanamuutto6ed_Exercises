from math import *
import numpy as np

#single stage turbine on free vortex theory
m_dot = 36 #[kg/s]
T_01 = 1200 #[K]
p_01 = 8 #[bar]
deltaT_013 = 150 #[K]
eta_t = 0.9
U_m = 320 #[m/s]
N = 250 #[rev/s]
V3 = 400 #[m/s] axial
alpha_3 = radians(0) #[radians]

#Calculate:
#blade height and radius ratio of the annulus from the outlet conditions
#Assuming nozzle loss below, calculate the inlet Mach number relative to the rotor blade at the root radius
nozzle_loss = 0.07
V2a = 346 #[m/s]

#constant
cp = 1148
gamma = 1.333
aux = gamma/(gamma-1)
R = 0.287

pr = 1/((-(deltaT_013/(eta_t*T_01) -1))**(aux))

p_03 = p_01/pr

T_03 = T_01 - deltaT_013
T_3 = T_03 - ((V3**2)/(2*cp))

p_3 = p_03*((T_3/T_03)**aux)

rho_3 = (p_3*100)/(R*T_3)

A = m_dot/(V3*rho_3)

r_m = U_m/(2*pi*N)

h = A/(2*pi*r_m)

print("Blade height: ", h)

r_root = r_m - (h/2)
r_tip = r_m + (h/2)
r_ratio = r_tip/r_root

print("Radius ratio: ", r_ratio)

U_r = 2*pi*N*r_root

flow_coeff_r = V2a/U_r
temp_drop_coeff_r = (2*cp*deltaT_013)/(U_r**2)

tg_beta_3_r = tan(alpha_3) + (1/flow_coeff_r)

tg_beta_2_r = (cp*deltaT_013/(U_r*V2a)) - tg_beta_3_r
beta_2_r = atan(tg_beta_2_r)

tg_alpha_2_r = (1/flow_coeff_r) + tg_beta_2_r
alpha_2_r = atan(tg_alpha_2_r)
V2 = V2a/cos(alpha_2_r)
W2 = V2a/cos(beta_2_r)
#reaction_r = ((tg_beta_3_r*2*flow_coeff_r) - (temp_drop_coeff_r/2))/2

#print(reaction_r)

T_02 = T_01 #no change in absolute temperature at nozzle
T_2_prime = T_02 - (V2**2)/(2*cp)
T_2 = T_2_prime + (nozzle_loss*((V2**2)/(2*cp)))


a = sqrt(gamma*R*T_2*1000)

M = W2/a
print("Relative Mach number at rotor inlet in root radius: ", M)