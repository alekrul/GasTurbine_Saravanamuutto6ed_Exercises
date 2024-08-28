from math import *

#given parameters
m_dot = 14 #[kg/s]
pr = 4
N = 200 #[rev/s]
T_a = 288 #[K]
p_a = 1 #[bar]
slip_factor = 0.9
power_input_factor = 1.04
eta = 0.8

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#calculate
#(a) overall diameter of the impeller
#(b) minimum possible axial depth of the diffuser, assuming M = 1 and 50% losses occur at impeller

U = sqrt(T_a*cp*((pr**(1/aux)) - 1)/(slip_factor*power_input_factor*eta))
dtip = U/(pi*N)

print("Diameter of impeller: ", dtip)

V2u = slip_factor*U
eta_imp = 1 - (0.5*(1-eta))
delta_T03_T01 = slip_factor*power_input_factor*U*U/cp
T_03 = T_a + delta_T03_T01

T_02 = T_03
#M=1 so:
T_2 = T_02*(2/(gamma+1))
a = sqrt(gamma*R*1000*T_2)

V2 = a

V2r = sqrt(V2**2 - V2u**2)

delta_T02_T01 = eta_imp*delta_T03_T01

p_02_p_01 = (1 + delta_T02_T01/T_a)**aux
p_02 = p_a*p_02_p_01

p_02_p_2 = ((gamma+1)/2)**aux
p_2 = p_02/p_02_p_2

rho_2 = p_2*100/(R*T_2)

A = m_dot/(rho_2*V2r)

h = A/(pi*dtip)

print("axial depth of the diffuser: ",h)