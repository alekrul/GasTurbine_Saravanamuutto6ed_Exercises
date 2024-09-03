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