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

root_coeff1 = deltaT*cp/(work_done_factor*Ur*Va)
mean_coeff1 = deltaT*cp/(work_done_factor*Um*Va)
tip_coeff1 = deltaT*cp/(work_done_factor*Ut*Va)

reaction_tip = 1 - (1/((Ut/Um)**2))*(1-reaction_m)
reaction_root = 1 - (1/((Ur/Um)**2))*(1-reaction_m)

print(reaction_root)
print(reaction_tip)

root_coeff2 = (reaction_root-1)*(-2)*Ur/Va
tip_coeff2 = (reaction_tip-1)*(-2)*Ut/Va
mean_coeff2 = (reaction_m-1)*(-2)*Um/Va

Am = np.array([[-1,1],[1,1]])
Bm = np.array([mean_coeff1,mean_coeff2])

Ar = np.array([[-1,1],[1,1]])
Br = np.array([root_coeff1,root_coeff2])

At = np.array([[-1,1],[1,1]])
Bt = np.array([tip_coeff1,tip_coeff2])

solution_t = np.linalg.solve(At, Bt)
solution_m = np.linalg.solve(Am, Bm)
solution_r = np.linalg.solve(Ar, Br)

alpha1_t = degrees(atan(solution_t[0]))
alpha1_r = degrees(atan(solution_r[0]))
alpha1_m = degrees(atan(solution_m[0]))

alpha2_t = degrees(atan(solution_t[1]))
alpha2_r = degrees(atan(solution_r[1]))
alpha2_m = degrees(atan(solution_m[1]))

beta2_m = alpha1_m
beta1_m = alpha2_m


root_coeff3 = reaction_root*2*Ur/Va
tip_coeff3 = reaction_tip*2*Ut/Va

Ar = np.array([[1,-1],[1,1]])
Br = np.array([root_coeff1,root_coeff3])

At = np.array([[1,-1],[1,1]])
Bt = np.array([tip_coeff1,tip_coeff3])

solution_t = np.linalg.solve(At, Bt)
solution_r = np.linalg.solve(Ar, Br)

beta1_t = degrees(atan(solution_t[0]))
beta1_r = degrees(atan(solution_r[0]))

beta2_t = degrees(atan(solution_t[1]))
beta2_r = degrees(atan(solution_r[1]))

print("Root:")
print("Alpha 1: ", alpha1_r)
print("Alpha 2: ", alpha2_r)
print("Beta 1: ", beta1_r)
print("Beta 2: ", beta2_r)
print("reaction: ", reaction_root)
print("-----------------")
print("Mean:")
print("Alpha 1: ", alpha1_m)
print("Alpha 2: ", alpha2_m)
print("Beta 1: ", beta1_m)
print("Beta 2: ", beta2_m)
print("reaction: ", reaction_m)
print("-----------------")
print("Tip:")
print("Alpha 1: ", alpha1_t)
print("Alpha 2: ", alpha2_t)
print("Beta 1: ", beta1_t)
print("Beta 2: ", beta2_t)
print("reaction: ", reaction_tip)