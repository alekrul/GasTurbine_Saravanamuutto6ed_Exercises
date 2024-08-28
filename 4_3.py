from math import *

#given parameters
p_03 = 2.97 #[bar]
T_03 = 429 #[K]
p_2 = 1.92 #[bar]
m_dot = 0.6 #[kg/s]
N = 766 #[rev/s]
p_a = 0.99 #[bar]
T_a = 288 #[K]

ri = 0.165/2 #[m]
l = 0.01 #[m]
n = 17

slip_factor = 1 - (0.63*pi/n) #Stanitz equation for slip factor

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#determine
#(a) overall isoentropic efficiency of the compressor
#(b)stagnation pressure at the impeller tip
#(c)fraction of the overral loss which occurs in the impeller

T_03_prime = T_a*((p_03/p_a)**(1/aux))

eta = (T_03_prime-T_a)/(T_03-T_a)

print("Isoentropic efficiency: ", eta)

Ut = N*2*pi*ri
V2u = slip_factor*Ut
T_02 = T_03 #since no work or heat is involved in the diffuser


A = 2*pi*ri*l
#A = pi*ri*ri
V2r = 10
max_it = 10
err = 0.01
for i in range(max_it):
    print("iteration: ", i)
    V2 = sqrt((V2u**2) + (V2r**2))
    T_2 = T_02 - (V2**2/(2*cp))
    rho_2 = p_2*100/(R*T_2)

    #checking
    V2r_check = m_dot/(rho_2*A)
    check = abs(V2r_check - V2r)/V2r
    V2r = V2r_check
    if(check<err):
        break

p_02 = p_2/((T_2/T_02)**aux)
print("Stagnation pressure at impeller tip:", p_02)

eta_imp = ((T_a*((p_02/p_a)**(1/aux))) - T_a)/(T_02-T_a)

loss = (1-eta_imp)/(1-eta)

print("Loss fraction at impeller:", loss)