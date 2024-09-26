from math import *
import numpy as np

#data
rm_rr_2 = 1.164
rm_rt_2 = 0.877

alpha_2_m = radians(58.38)
beta_2_m = radians(20.49)
alpha_3_m = radians(10.0)
beta_3_m = radians(54.96)

#data from 7.2 exercise
V3 = 275 #[m/s]
Ur = 300 #[m/s]
V1 = V3
Ur = 300 #[m/s]
eta_t = 0.88
pr = 2
T_01 = 1050 #[K]


#constant
cp = 1148
gamma = 1.333
aux = gamma/(gamma-1)
R = 0.287

#calculate beta2 at tip and root for constant nozzle angle design in which alpha2 and V2u*r are constant over the annulus

#if alpha2 is constant over the annulus, alpha2 = alpha_2_m (alpha at mean diameter)

alpha_2 = alpha_2_m

Um_Vam = tan(alpha_2) - tan(beta_2_m)
flow_coeff_m =  1/Um_Vam
print(Um_Vam)
print(flow_coeff_m)

tg_beta_2_r = tan(alpha_2) - Um_Vam*((1/rm_rr_2)**2)
beta_2_r = atan(tg_beta_2_r)
print(degrees(beta_2_r))

tg_beta_2_t = tan(alpha_2) - Um_Vam*((1/rm_rt_2)**2)
beta_2_t = atan(tg_beta_2_t)
print(degrees(beta_2_t))

#now considering Vt*r**x where x = sin**2 alpha

x = sin(alpha_2)**2

tg_beta_2_r_new = tan(alpha_2) - Um_Vam*((1/rm_rr_2)**(x+1))
beta_2_r_new = atan(tg_beta_2_r_new)
print(degrees(beta_2_r_new))

tg_beta_2_t_new = tan(alpha_2) - Um_Vam*((1/rm_rt_2)**(x+1))
beta_2_t_new = atan(tg_beta_2_t_new)
print(degrees(beta_2_t_new))
