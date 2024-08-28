from math import *

#given parameters
rr = 0.18/2 #[m] eye root radius
rt = 0.33/2 #[m] eye tip radius
rimp = 0.54/2 #[m] impeller periphery radius
m_dot = 3.6 #[kg/s]
T_a = 217 #[K]
p_a = 0.23 #[bar]
N = 270 #[rev/s]
alpha0 = 25 #[degrees] pre-whirl
V1 = 230 #[m/s]

#assumptions
eta_c = 0.8
slip_factor = 0.9
power_input_factor = 1.04

#constant
cp = 1005
gamma = 1.4
aux = gamma/(gamma-1)
R = 0.287

#calculate stagnation pressure at the compressor outlet

T01 = T_a + (V1**2)/(2*cp)
p01 = p_a*((T01/T_a)**aux)

U2 = 2*pi*rimp*N
V1t = V1*sin(radians(alpha0))
U1 = 2*pi*rr*N

delta_T03_T01 = power_input_factor*(slip_factor*(U2**2) - U1*V1t)/cp
p03 = p01*((1 + eta_c*delta_T03_T01/T01)**aux)

print(p03)