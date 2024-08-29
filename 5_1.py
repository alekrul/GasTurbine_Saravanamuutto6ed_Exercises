from math import *
import numpy as np


#given parameters
Ur = 150 #[m/s]
Um = 200 #[m/s]
Ut = 250 #[m/s]
deltaT = 20 #[K]
Va = 150 #[m/s]
work_done_factor = 0.93
reaction_m = 0.5

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#calculate
#(a) air angles at root, mean and tip
#(b) degree of reaction at root and tip
#free vortex design

