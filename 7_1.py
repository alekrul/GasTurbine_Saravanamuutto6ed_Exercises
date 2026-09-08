"""
Saravanamuttoo - Gas Turbine Theory (6th ed.)
Exercise 7.1  -  Mean-diameter axial turbine stage

Given a single axial turbine stage, determine:
    * rotor-blade gas angles (beta_2, beta_3)
    * degree of reaction (Lambda)
    * temperature-drop / loading coefficient (psi)
    * power output (P)

A combined velocity diagram is drawn and saved as an image.
"""

from math import tan, atan, cos, radians, degrees
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# INPUT DATA
# --------------------------------------------------------------------------
m_dot  = 20.0            # mass flow rate                 [kg/s]
T01    = 1000.0          # stage inlet stagnation temp.   [K]
p01    = 4.0             # stage inlet stagnation press.  [bar]
Ca     = 260.0           # axial velocity (constant)      [m/s]
U      = 360.0           # blade speed at mean diameter   [m/s]
alpha2 = radians(65.0)   # nozzle efflux angle            [deg]
alpha3 = radians(10.0)   # stage exit swirl angle         [deg]

cp     = 1148.0          # specific heat, combustion gas  [J/kg.K]
gamma  = 1.333           # ratio of specific heats        [-]
R      = 287.0           # gas constant                   [J/kg.K]

# Loss coefficients (temperature-loss definition, e.g. lambda_N = (T2 - T2')/(C2^2/2cp))
lambda_N = 0.05          # nozzle loss coefficient        [-]
lambda_R = 0.05          # rotor  loss coefficient        [-]  <-- set to your value
# Alternatively, if you prefer to impose a stage total-to-total efficiency instead
# of a rotor loss, set eta_s below to a number (e.g. 0.90); leave as None to use lambda_R.
eta_s    = None          # stage total-to-total efficiency [-] or None

n = gamma / (gamma - 1.0)   # isentropic exponent p/T grouping

# --------------------------------------------------------------------------
# 1) ROTOR-BLADE GAS ANGLES
#    Combining the inlet/outlet velocity triangles (Ca constant):
#        tan(beta_2) = tan(alpha_2) - U/Ca
#        tan(beta_3) = tan(alpha_3) + U/Ca
# --------------------------------------------------------------------------
tan_b2 = tan(alpha2) - U / Ca
tan_b3 = tan(alpha3) + U / Ca
beta2  = atan(tan_b2)
beta3  = atan(tan_b3)

# --------------------------------------------------------------------------
# 2) DEGREE OF REACTION
#        Lambda = (Ca / 2U) * (tan(beta_3) - tan(beta_2))
# --------------------------------------------------------------------------
reaction = (Ca / (2.0 * U)) * (tan_b3 - tan_b2)

# --------------------------------------------------------------------------
# 3) TEMPERATURE-DROP (STAGE LOADING) COEFFICIENT
#        psi = 2 * cp * dT0s / U^2 = 2 * (Ca / U) * (tan(beta_2) + tan(beta_3))
# --------------------------------------------------------------------------
psi     = 2.0 * (Ca / U) * (tan_b2 + tan_b3)
dT0s    = psi * U**2 / (2.0 * cp)      # stage stagnation temperature drop [K]

# --------------------------------------------------------------------------
# 4) POWER OUTPUT
#        P = m_dot * cp * dT0s = m_dot * U * Ca * (tan(beta_2) + tan(beta_3))
# --------------------------------------------------------------------------
power = m_dot * cp * dT0s              # [W]

# --------------------------------------------------------------------------
# Velocity components (for the diagram and for reference)
#   +tangential direction = blade motion (U)
# --------------------------------------------------------------------------
Cw2 =  Ca * tan(alpha2)     # absolute whirl at nozzle exit  (with U)
Vw2 =  Ca * tan_b2          # relative whirl at rotor inlet   (with U)
Vw3 = -Ca * tan_b3          # relative whirl at rotor exit    (against U)
Cw3 =  Vw3 + U              # absolute whirl at stage exit    (against U)

C2  = Ca / cos(alpha2)
V2  = Ca / cos(beta2)
V3  = Ca / cos(beta3)
C3  = Ca / cos(alpha3)

# --------------------------------------------------------------------------
# 5) NOZZLE THROAT AREA  (using the nozzle loss coefficient lambda_N)
#    T02 = T01 (no work in the nozzle).  The isentropic static temperature
#    T2' fixes the static pressure through the nozzle loss:
#        T2  = T02 - C2^2 / (2 cp)
#        T2' = T2  - lambda_N * C2^2 / (2 cp)
#        p01 / p2 = (T01 / T2')^(gamma/(gamma-1))
#
#    A convergent nozzle chokes when p2 falls to (or below) the critical
#    pressure p_c.  If choked, the throat sits at critical (M = 1) conditions;
#    otherwise the throat equals the nozzle-exit conditions.
# --------------------------------------------------------------------------
T02 = T01
T2  = T02 - C2**2 / (2.0 * cp)
T2p = T2 - lambda_N * C2**2 / (2.0 * cp)      # isentropic static temperature
p2  = p01 / (T01 / T2p) ** n                  # nozzle-exit static pressure [bar]
p01_over_p2 = p01 / p2

# Critical (throat, M=1) conditions, including the nozzle loss up to the throat
Tc   = T01 * 2.0 / (gamma + 1.0)                       # critical static temp
p01_over_pc = (1.0 - (1.0 + lambda_N) *
               (gamma - 1.0) / (gamma + 1.0)) ** (-n)  # critical press. ratio
pc   = p01 / p01_over_pc                               # critical pressure [bar]
choked = p2 <= pc

if choked:
    T_th   = Tc
    p_th   = pc
    C_th   = (gamma * R * T_th) ** 0.5        # = local sonic speed (M = 1)
else:
    T_th   = T2
    p_th   = p2
    C_th   = C2
rho_th   = p_th * 1e5 / (R * T_th)            # throat density [kg/m3]
A_throat = m_dot / (rho_th * C_th)            # nozzle throat area [m2]

# --------------------------------------------------------------------------
# 6) TURBINE-STAGE PRESSURE RATIO  p01 / p03  (needs the rotor loss lambda_R,
#    or, equivalently, a stage total-to-total efficiency eta_s)
#
#    If eta_s is given:  p01/p03 = [1 - dT0s/(eta_s*T01)]^(-gamma/(gamma-1))
#    Otherwise, from lambda_R:
#        T3   = T03 - C3^2/(2cp)
#        T3'  = T3  - lambda_R * V3^2/(2cp)      (rotor isentropic static temp)
#        p2/p3 = (T2/T3')^(gamma/(gamma-1))      -> static pressure p3
#        p03   = p3 * (T03/T3)^(gamma/(gamma-1))
# --------------------------------------------------------------------------
T03 = T01 - dT0s

if eta_s is not None:
    p01_over_p03 = (1.0 - dT0s / (eta_s * T01)) ** (-n)
    p03 = p01 / p01_over_p03
    eta_tt = eta_s
    # back out static pressures for completeness
    T3  = T03 - C3**2 / (2.0 * cp)
    p3  = p03 / (T03 / T3) ** n
else:
    T3   = T03 - C3**2 / (2.0 * cp)
    T3p  = T3 - lambda_R * V3**2 / (2.0 * cp)
    p3   = p2 / (T2 / T3p) ** n
    p03  = p3 * (T03 / T3) ** n
    p01_over_p03 = p01 / p03
    # resulting total-to-total isentropic efficiency
    eta_tt = dT0s / (T01 * (1.0 - (p03 / p01) ** (1.0 / n)))

p01_over_p3 = p01 / p3        # stagnation-to-static (rotor-exit) ratio

# --------------------------------------------------------------------------
# PRETTY-PRINTED RESULTS
# --------------------------------------------------------------------------
line = "=" * 60


def header(title):
    print(f"\n{line}\n{title.center(60)}\n{line}")


header("EXERCISE 7.1  -  MEAN-DIAMETER AXIAL TURBINE STAGE")

print("\nInput data")
print("-" * 60)
print(f"  {'Mass flow rate':32s} m_dot  = {m_dot:8.2f}  kg/s")
print(f"  {'Inlet stagnation temperature':32s} T01    = {T01:8.2f}  K")
print(f"  {'Inlet stagnation pressure':32s} p01    = {p01:8.2f}  bar")
print(f"  {'Axial velocity':32s} Ca     = {Ca:8.2f}  m/s")
print(f"  {'Blade speed (mean)':32s} U      = {U:8.2f}  m/s")
print(f"  {'Nozzle efflux angle':32s} alpha2 = {degrees(alpha2):8.2f}  deg")
print(f"  {'Stage exit swirl angle':32s} alpha3 = {degrees(alpha3):8.2f}  deg")

print("\nVelocity components  (+ve = direction of blade motion)")
print("-" * 60)
print(f"  Cw2 = {Cw2:8.2f} m/s     C2 = {C2:8.2f} m/s")
print(f"  Vw2 = {Vw2:8.2f} m/s     V2 = {V2:8.2f} m/s")
print(f"  Vw3 = {Vw3:8.2f} m/s     V3 = {V3:8.2f} m/s")
print(f"  Cw3 = {Cw3:8.2f} m/s     C3 = {C3:8.2f} m/s")

header("RESULTS")
print(f"  {'Rotor inlet gas angle':38s} beta_2   = {degrees(beta2):7.2f}  deg")
print(f"  {'Rotor outlet gas angle':38s} beta_3   = {degrees(beta3):7.2f}  deg")
print(f"  {'Degree of reaction':38s} Lambda   = {reaction:7.3f}")
print(f"  {'Temperature-drop coefficient':38s} psi      = {psi:7.3f}")
print(f"  {'Stage stagnation temperature drop':38s} dT0s     = {dT0s:7.2f}  K")
print(f"  {'Power output':38s} P        = {power/1e6:7.3f}  MW")
print(line)

header("NOZZLE THROAT  &  STAGE PRESSURE RATIO")
print(f"\nNozzle (station 2), lambda_N = {lambda_N:.2f}")
print("-" * 60)
print(f"  {'Nozzle exit velocity':34s} C2          = {C2:8.2f}  m/s")
print(f"  {'Nozzle exit static temperature':34s} T2          = {T2:8.2f}  K")
print(f"  {'Nozzle exit static pressure':34s} p2          = {p2:8.4f}  bar")
print(f"  {'Nozzle static pressure ratio':34s} p01/p2      = {p01_over_p2:8.4f}")
print(f"  {'Critical (throat) pressure':34s} p_c         = {pc:8.4f}  bar")
print(f"  {'Nozzle flow is':34s}               {'CHOKED (throat at M=1)' if choked else 'un-choked'}")
print(f"  {'Throat static temperature':34s} T_th        = {T_th:8.2f}  K")
print(f"  {'Throat velocity':34s} C_th        = {C_th:8.2f}  m/s")
print(f"  {'Throat density':34s} rho_th      = {rho_th:8.4f}  kg/m3")
print(f"  {'NOZZLE THROAT AREA':34s} A_throat    = {A_throat:8.5f}  m2")

if eta_s is not None:
    src = f"eta_s = {eta_s:.3f} (given)"
else:
    src = f"lambda_R = {lambda_R:.2f} (given)"
print(f"\nStage pressure ratio   [{src}]")
print("-" * 60)
print(f"  {'Rotor exit static temperature':34s} T3          = {T3:8.2f}  K")
print(f"  {'Rotor exit static pressure':34s} p3          = {p3:8.4f}  bar")
print(f"  {'Stage exit stagnation pressure':34s} p03         = {p03:8.4f}  bar")
print(f"  {'Stage-to-static pressure ratio':34s} p01/p3      = {p01_over_p3:8.4f}")
print(f"  {'STAGE PRESSURE RATIO (total)':34s} p01/p03     = {p01_over_p03:8.4f}")
print(f"  {'Stage total-to-total efficiency':34s} eta_tt      = {eta_tt:8.4f}")
print(line)


# --------------------------------------------------------------------------
# COMBINED VELOCITY DIAGRAM
#   Single common apex O at the top; axial velocity Ca is common to all
#   four vectors, so every vector tip lies on the line y = -Ca.
#   Inlet triangle (C2, V2, U) on the right; exit triangle (V3, C3, U)
#   on the left.  x = whirl (tangential), y = -axial.
# --------------------------------------------------------------------------
def draw_diagram():
    O = (0.0, 0.0)
    y = -Ca

    tips = {          # (x, y, colour, label)
        "C2": (Cw2, y, "#c0392b"),
        "V2": (Vw2, y, "#2471a3"),
        "C3": (Cw3, y, "#e67e22"),
        "V3": (Vw3, y, "#16a085"),
    }

    fig, ax = plt.subplots(figsize=(10, 6.5))

    # velocity vectors from the common apex
    for name, (x, yy, col) in tips.items():
        ax.annotate("", xy=(x, yy), xytext=O,
                    arrowprops=dict(arrowstyle="-|>", lw=2.2, color=col))

    # blade-speed U segments (along the tip line y = -Ca)
    ax.annotate("", xy=(Cw2, y), xytext=(Vw2, y),
                arrowprops=dict(arrowstyle="-|>", lw=2.4, color="#7d3c98"))
    ax.annotate("", xy=(Cw3, y), xytext=(Vw3, y),
                arrowprops=dict(arrowstyle="-|>", lw=2.4, color="#7d3c98"))

    # axial reference line
    ax.plot([0, 0], [0, y], ls="--", lw=1.2, color="grey")
    ax.plot([Vw3, Cw2], [y, y], ls="-", lw=0.8, color="grey", zorder=0)

    # vector labels (mid-vector)
    def lbl(name, x, yy, col, dx=0, dy=0):
        ax.text(x / 2 + dx, yy / 2 + dy, name, color=col,
                fontsize=13, fontweight="bold", ha="center", va="center")

    lbl("C2", Cw2, y, "#c0392b", dx=18)
    lbl("V2", Vw2, y, "#2471a3", dx=-22)
    lbl("C3", Cw3, y, "#e67e22", dx=-16, dy=6)
    lbl("V3", Vw3, y, "#16a085", dx=-20)
    ax.text((Vw2 + Cw2) / 2, y - 14, "U", color="#7d3c98",
            fontsize=13, fontweight="bold", ha="center")
    ax.text((Vw3 + Cw3) / 2, y - 14, "U", color="#7d3c98",
            fontsize=13, fontweight="bold", ha="center")
    ax.text(6, y / 2, "Ca", color="grey", fontsize=11, ha="left", va="center")

    # apex marker
    ax.plot(*O, "ko", ms=5)
    ax.text(0, 12, "O", fontsize=11, ha="center")

    ax.set_title("Exercise 7.1 - Combined Velocity Diagram\n"
                 fr"$\beta_2$={degrees(beta2):.1f}$\degree$, "
                 fr"$\beta_3$={degrees(beta3):.1f}$\degree$, "
                 fr"$\Lambda$={reaction:.2f}, "
                 fr"$\psi$={psi:.2f}",
                 fontsize=13)
    ax.set_xlabel("whirl velocity  [m/s]")
    ax.set_ylabel("axial velocity  [m/s]")
    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(True, ls=":", alpha=0.4)

    # legend
    handles = [plt.Line2D([], [], color=c, lw=2.4, label=n)
               for n, c in [("C - absolute (nozzle exit / stage exit)", "#c0392b"),
                            ("V - relative (rotor inlet / outlet)", "#2471a3"),
                            ("U - blade speed", "#7d3c98")]]
    ax.legend(handles=handles, loc="upper left", fontsize=9, framealpha=0.9)

    fig.tight_layout()
    out = "7_1_velocity_diagram.png"
    fig.savefig(out, dpi=150)
    print(f"\nVelocity diagram saved to '{out}'")
    plt.show()


draw_diagram()
