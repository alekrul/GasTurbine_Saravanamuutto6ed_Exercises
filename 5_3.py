from math import *
import numpy as np

#no inlet guide vanes
#free vortex
N = 6000 #[rev/min]
deltaT = 20 #[K]
rt_ratio = 0.6
work_done_factor = 0.93
eta = 0.89
V1 = 140 #[m/s]
p_a = 1.01 #[bar]
T_a = 288 #[K]

Mrel_tip = 0.95

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#find:
#(a) tip radius and rotor air angles
#(b) mass flow
#(c) stage stagnation pressure ration and power required
#(d) rotor air angles at root section

Va1 = V1 #Vt1 is zero
T_1 = T_a - (V1**2/(2*cp))
a = sqrt(T_1*R*gamma*1000)
Utip = sqrt((a*Mrel_tip)**2 - V1**2)

rtip = Utip/(N*2*pi*(1/60))

print("Tip radius:", rtip)

deltaV = cp*deltaT/(work_done_factor*Utip)

beta1_t = atan(Utip/V1)
beta2_t = atan((Utip-deltaV)/V1)
print("Beta 1 at tip:", degrees(beta1_t))
print("Beta 2 at tip:", degrees(beta2_t))

rroot = rtip*rt_ratio

p_1 = p_a*((T_1/T_a)**aux)
rho_1 = p_1*100/(T_1*R)

m_dot = rho_1*V1*pi*(rtip**2 - rroot**2)

print("Mass flow: ", m_dot)

p_ratio = (1 + eta*deltaT/T_a)**aux

W_req = m_dot*Utip*deltaV*work_done_factor

print("Pressure ratio: ", p_ratio)
print("Work required: ", W_req)

Uroot = Utip*rt_ratio

beta1_r = atan(Uroot/V1)

deltaV_r = cp*deltaT/(work_done_factor*Uroot)

beta2_r = atan((Uroot-deltaV_r)/V1)

print("Beta 1 at root:", degrees(beta1_r))
print("Beta 2 at root:", degrees(beta2_r))