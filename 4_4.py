from math import *

#given parameters
rimp = 0.5/2 #[m] outer radius of impeller
N = 270 #[rev/s]
m_dot = 16 #[kg/s]
T_a = 288 #[K]
p_a = 1.01 #[bar]
eta_imp = 0.9
power_input_factor = 1.04
slip_factor = 0.9
b = 0.05 #[m] depth vaneless space
l = 0.04 #[m] gap vaneless space

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#evaluate:
#(a) stagnation pressure and temperature at outlet of impeller, assuming no pre-whirl
#(b) show that radial outlet velocity at impeller tip is 96 m/s, find M and air leaving angle
#(c) find correct angle of the leading edges of the diffuser vanes and M at this radius


U = N*2*pi*rimp
delta_T03_T01 = power_input_factor*slip_factor*(U**2)/cp

T_03 = T_a + delta_T03_T01
T_02 = T_03
T_02prime = delta_T03_T01*eta_imp + T_a

p_02 = p_a*((T_02prime/T_a)**aux)

print("Stagnation pressure at impeller tip:", p_02)

Atip = 2*pi*rimp*b
V2u = slip_factor*U

#assuming V2r = 96 m/s to show that converges
V2r = 96
V2 = sqrt((V2r**2) + (V2u**2))

T_2 = T_02 - ((V2**2)/(2*cp))
p_2 = p_02*((T_2/T_02)**aux)

rho_2 = p_2*100/(T_2*R)

#checking
V2r_check = m_dot/(rho_2*Atip)

diff = (V2r_check-V2r)/V2r

print("Difference: ", diff*100, "%")

alpha2 = atan(V2r/V2u)
print("Angle: ", degrees(alpha2))

a = sqrt(gamma*R*1000*T_2)
M = V2/a
print("M: ", M)

rd = rimp + l
Vdu = V2u*(rimp/rd)

#estimating Vd

Vdr = 10
max_it = 10
err = 0.01

Ad = 2*pi*rd*b
T_0d = T_02
for i in range(max_it):
    Vd = sqrt((Vdu**2) + (Vdr**2))
    T_d = T_0d - (Vd**2/(2*cp))
    p_02_p_01 = p_02/p_a
    p_2 = p_a*p_02_p_01*((T_d/T_0d)**aux)
    rho_d = p_2*100/(R*T_d)
    #check
    Vdr_check = m_dot/(rho_d*Ad)
    
    check = abs(Vdr_check - Vdr)/Vdr
    Vdr = Vdr_check
    if(check<err):
        break

alphad = atan(Vdr/Vdu)
print("angle at diffuser: ", degrees(alphad))

a_d = sqrt(gamma*R*1000*T_d)
M = sqrt(Vdr**2 + Vdu**2)/a_d

print("M at diffuser: ", M)