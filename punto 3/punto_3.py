import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# CONFIGURACIÓN
# ============================================================

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"
CARPETA_GRAFICAS.mkdir(exist_ok=True)


# ============================================================
# ECUACIÓN DIFERENCIAL
# P' = P(P-1)(2-P)
# ============================================================

def f(P):
    return P * (P - 1) * (2 - P)


# ============================================================
# PUNTOS CRÍTICOS
# ============================================================

puntos_criticos = [0, 1, 2]


# ============================================================
# DIAGRAMA DE FASE
# ============================================================

t = np.linspace(0, 10, 25)
P = np.linspace(-0.5, 2.8, 25)

T, PP = np.meshgrid(t, P)

valores = f(PP)

# Normalización de las pendientes
U = np.ones_like(valores)
V = valores

norma = np.sqrt(U**2 + V**2)

U = U / norma
V = V / norma


fig, ax = plt.subplots(figsize=(10, 7))

ax.quiver(
    T,
    PP,
    U,
    V,
    angles="xy",
    pivot="mid",
    alpha=0.45
)


# Equilibrios
for punto in puntos_criticos:
    ax.axhline(
        punto,
        linestyle="--",
        linewidth=2,
        label=f"P = {punto}"
    )


ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 2.8)

ax.set_xlabel("t (años)")
ax.set_ylabel("P (miles de ejemplares)")

ax.set_title(
    r"Diagrama de fase: $P'=P(P-1)(2-P)$"
)

ax.grid(True, alpha=0.25)

ax.legend()

plt.tight_layout()

ruta_fase = CARPETA_GRAFICAS / "3_diagrama_fase_poblacion.png"

plt.savefig(
    ruta_fase,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(f"Gráfica creada: {ruta_fase}")


# ============================================================
# SOLUCIONES PARA DIFERENTES CONDICIONES INICIALES
# ============================================================

def rk4(P0, t_max=12, h=0.01):

    n = int(t_max / h) + 1

    tiempos = np.linspace(0, t_max, n)

    poblacion = np.zeros(n)

    poblacion[0] = P0

    for i in range(n - 1):

        P_actual = poblacion[i]

        k1 = f(P_actual)

        k2 = f(P_actual + h * k1 / 2)

        k3 = f(P_actual + h * k2 / 2)

        k4 = f(P_actual + h * k3)

        poblacion[i + 1] = (
            P_actual
            + h * (k1 + 2*k2 + 2*k3 + k4) / 6
        )

    return tiempos, poblacion


# Condiciones iniciales
condiciones = [
    (3, "P(0)=3 → 3000 ejemplares"),
    (1.5, "P(0)=1.5 → 1500 ejemplares"),
    (0.5, "P(0)=0.5 → 500 ejemplares"),
    (0.9, "P(0)=0.9 → 900 ejemplares")
]


fig, ax = plt.subplots(figsize=(10, 7))


for P0, etiqueta in condiciones:

    tiempos, poblacion = rk4(P0)

    ax.plot(
        tiempos,
        poblacion,
        linewidth=2,
        label=etiqueta
    )


# Líneas de equilibrio
for punto in puntos_criticos:

    ax.axhline(
        punto,
        linestyle="--",
        linewidth=1.5,
        label=f"Equilibrio P={punto}"
    )


ax.set_xlabel("t (años)")

ax.set_ylabel(
    "P (miles de ejemplares)"
)

ax.set_title(
    r"Comportamiento de la población: $P'=P(P-1)(2-P)$"
)

ax.set_ylim(-0.05, 3.15)

ax.grid(True, alpha=0.25)

ax.legend()

plt.tight_layout()


ruta_soluciones = (
    CARPETA_GRAFICAS
    / "3_soluciones_condiciones_iniciales.png"
)

plt.savefig(
    ruta_soluciones,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print(
    f"Gráfica creada: {ruta_soluciones}"
)


# ============================================================
# FINAL
# ============================================================

print()
print("=" * 60)
print("TODAS LAS GRÁFICAS DEL PUNTO 3 FUERON GENERADAS")
print("=" * 60)
print()
print("Archivos:")
print("✓ 3_diagrama_fase_poblacion.png")
print("✓ 3_soluciones_condiciones_iniciales.png")