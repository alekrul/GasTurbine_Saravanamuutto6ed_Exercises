from math import *

#given parameters
rr = 0.065 #[m] eye root radius
rt = 0.15 #[m] eye tip radius
m_dot = 8 #[kg/s]
T_a = 288 #[K]
p_a = 1 #[bar]
N = 270 #[rev/s]

#assumptions
Vte = 0 #no pre-whirl, axial flow at inlet

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#calculate
#(a) blade inlet angle at root and tip of the eye
#(b) Mach number at tip of the eye

Ur = N*rr*2*pi
Ut = N*rt*2*pi
A = pi*(rt**2 - rr**2)

#need to estimate V = Va

V1a = 90 #initial guess
V1 = V1a #because there is no pre whirl

max_it = 10
err = 0.01
for i in range(max_it):
    T_1 = T_a - (V1a**2/(2*cp))
    p_1 = p_a*((T_1/T_a)**aux)
    rho_1 = p_1*100/(R*T_1)

    #checking
    V1_check = m_dot/(rho_1*A)
    check = abs(V1_check - V1)/V1
    V1 = V1_check
    if(check<err):
        break

alpha_r = atan(V1/Ur)
alpha_t = atan(V1/Ut)

print("Alpha at eye root: ", degrees(alpha_r))
print("Alpha at eye tip: ", degrees(alpha_t))

#evaluating M
Wt = sqrt((V1**2)+(Ut**2))
a = sqrt(gamma*R*1000*T_1)
M = Wt/a

print("Mach number at eye tip: ", M)