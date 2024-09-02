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

print(rtip)

