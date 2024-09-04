from math import *
import numpy as np


pr = 4
m_dot = 3 #[kg/s]
eta_poli = 0.88
deltaT_0s = 25 #[K]
T_01 = 288 #[K]
p_01 = 1.01 #[bar]

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287
aux_poli = 1/(eta_poli*aux)

#calculate
#number of stages and pressure ratio of first and last stages

p_02 = p_01*pr
T_02 = T_01*((p_02/p_01)**aux_poli)

n_stages = (T_02-T_01)/deltaT_0s
n_stages = round(n_stages)

print("Number of stages: ", n_stages)

deltaT_0s = (T_02-T_01)/n_stages #correcting deltaT per stage after rounding up the number of stages

p_s = np.zeros(n_stages+1)
T_s = np.zeros(n_stages+1)

p_s[0] = p_01
T_s[0] = T_01

for i in range(n_stages):
    T_s[i+1] = T_s[i]+deltaT_0s
    p_s[i+1] = p_s[i]*((T_s[i+1]/T_s[i])**(1/aux_poli))

print(T_s)
print(p_s)

#(b) calculate rotational speed and length of the last stage rotot blade at inlet to the stage
V1_s7 = 165 #[m/s]
alpha1_s7 = radians(20) 
work_done_factor = 0.83
d_mean = 0.18 #[m]


Va1_s7 = V1_s7*cos(alpha1_s7)
V1u_s7 = V1_s7*sin(alpha1_s7)

#assuming symm vel. diagram:
W2_s7 = V1_s7
beta2_s7 = alpha1_s7

from sympy import symbols, Eq, solve

U, tg_beta1 = symbols('U tg_beta1')

#reaction 0.5 at mean:

b1 = Va1_s7*tan(beta2_s7)
b2 = deltaT_0s*cp/(work_done_factor*Va1_s7)

eq1 = Eq(U - Va1_s7*tg_beta1,b1)
eq2 = Eq(U*tg_beta1 - U*tan(alpha1_s7),b2)


solutions = solve((eq1, eq2), (U, tg_beta1))

U = [value[0] for value in solutions if value[0] > 0]
tg_beta1 = [value[1] for value in solutions if value[1] > 0]

N = U[0]/(pi*d_mean)

print("Rotational speed: ", N)

#length

T_1 = T_s[n_stages-1] - (V1_s7**2)/(2*cp)
p_1 = p_s[n_stages]*((T_1/T_s[n_stages])**aux)
rho_1 = p_1*100/(T_1*R)
A = m_dot/(rho_1*Va1_s7)
l = A/(pi*d_mean)

print("Length: ",l)

