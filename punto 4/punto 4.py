
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

"""
=============================================================================
SOLUCIÓN DEL PUNTO 4 (Incisos a, b y c) - MODELO POBLACIONAL
Ecuación diferencial: dP/dt = 3P - 2P^2
=============================================================================
Este script imprime el análisis matemático detallado en la consola y genera
una gráfica con el campo de pendientes y las curvas solución para visualización.
Ideal para correr y previsualizar en entornos como GitHub (con Jupyter/Markdown) 
o cualquier IDE de Python.
"""

def imprimir_analisis():
    """Imprime el desarrollo analítico de los incisos a, b y c de forma impecable."""
    reporte = """
======================================================================
ANÁLISIS MATEMÁTICO Y COMPORTAMIENTO POBLACIONAL
======================================================================
Modelo: dP/dt = 3P - 2P^2
Donde 'P' representa la población en miles y 't' el tiempo en años.

--- a) Diagrama de Fase y Análisis de Estabilidad ---
1. Puntos Críticos (Equilibrio):
   Se obtiene al igualar la tasa de cambio a cero: dP/dt = 0.
   P(3 - 2P) = 0  =>  P1 = 0  y  P2 = 1.5 (1500 ejemplares).

2. Comportamiento del Flujo (Signo de la derivada):
   - Intervalo 0 < P < 1.5: dP/dt > 0  => Crecimiento (Flecha a la derecha).
   - Intervalo P > 1.5:     dP/dt < 0  => Decrecimiento (Flecha a la izquierda).

3. Clasificación:
   - P = 0:   Punto Inestable (Repulsor). Las soluciones se alejan de él.
   - P = 1.5: Punto Estable (Atractor). Representa la capacidad de carga.

--- b) Población inicial de 2000 ejemplares (P(0) = 2) ---
Análisis: 
Como la población inicial P(0) = 2 es mayor que la capacidad de carga (1.5), 
la tasa de cambio es negativa (dP/dt < 0). 
Conclusión: 
La población decrecerá asintóticamente con el tiempo y se estabilizará 
exactamente en 1500 ejemplares (P = 1.5).

--- c) Población inicial de 100 especímenes (P(0) = 0.1) ---
Análisis: 
Como P(0) = 0.1 está entre 0 y 1.5, la tasa de cambio es positiva (dP/dt > 0). 
Conclusión: 
La especie cuenta con recursos para expandirse. La población crecerá de 
manera continua (curva sigmoide) hasta estabilizarse en 1500 ejemplares.
======================================================================
    """
    print(reporte)


def dPdt(t, P):
    """Define la ecuación diferencial para el integrador numérico."""
    return 3*P - 2*P**2


def graficar_soluciones():
    """Genera el campo de pendientes y las curvas solución de los incisos."""
    plt.figure(figsize=(10, 6))

    # 1. Crear el Campo de Pendientes (Slope Field)
    t_vals = np.linspace(0, 5, 25)
    P_vals = np.linspace(-0.2, 2.5, 25)
    T, P_grid = np.meshgrid(t_vals, P_vals)
    
    U = np.ones_like(T)
    V = dPdt(T, P_grid)
    
    # Normalización para unificar el tamaño de las flechas
    N = np.sqrt(U**2 + V**2)
    N[N == 0] = 1 
    U, V = U / N, V / N
    
    plt.quiver(T, P_grid, U, V, color='lightgray', angles='xy', label='Campo de pendientes')

    # 2. Dibujar las líneas de los Puntos Críticos (Equilibrio)
    plt.axhline(1.5, color='green', linestyle='--', linewidth=2.5, label='P = 1.5 (Estable / Capacidad de carga)')
    plt.axhline(0, color='red', linestyle='--', linewidth=2.5, label='P = 0 (Inestable / Extinción)')

    # 3. Resolver y graficar las condiciones iniciales
    t_eval = np.linspace(0, 5, 200)

    # Inciso b: P(0) = 2.0 (2000 ejemplares)
    sol_b = solve_ivp(dPdt, [0, 5], [2.0], t_eval=t_eval)
    plt.plot(sol_b.t, sol_b.y[0], 'b-', linewidth=3, label='b) P(0) = 2.0 (Decrece)')

    # Inciso c: P(0) = 0.1 (100 ejemplares)
    sol_c = solve_ivp(dPdt, [0, 5], [0.1], t_eval=t_eval)
    plt.plot(sol_c.t, sol_c.y[0], 'm-', linewidth=3, label='c) P(0) = 0.1 (Crece)')

    # Puntos de inicio
    plt.scatter([0, 0], [2.0, 0.1], color='black', zorder=5)

    # 4. Ajustes estéticos y renderizado
    plt.title('Diagrama de Fase y Soluciones: dP/dt = 3P - 2P²', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (años)', fontsize=12)
    plt.ylabel('Población P (en miles)', fontsize=12)
    plt.ylim(-0.2, 2.5)
    plt.xlim(0, 5)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper right', fontsize=10, shadow=True)
    plt.tight_layout()

    plt.show()

# ==========================================
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# ==========================================
if __name__ == '__main__':
    imprimir_analisis()
    graficar_soluciones()
    # PUNTO 4 - MODELO DE POBLACIÓN
# ============================================================

# Ecuación original:
# dP/dt = 3P - 2P^2


# ------------------------------------------------------------
# 4.d) Población de 1500 ejemplares
# ------------------------------------------------------------

def punto_4d():
    """
    Analiza el comportamiento de una población de 1500 ejemplares.

    Cuando la población alcanza los 1500 ejemplares,
    la tasa de cambio es igual a cero. Por lo tanto,
    no existe crecimiento ni disminución de la población.

    1500 ejemplares = 1.5 miles de ejemplares.

    La solución correspondiente es una población constante:
        P(t) = 1.5
    """

    print("4.d) Análisis de una población de 1500 ejemplares")
    print()
    print("Cuando la población alcanza los 1500 ejemplares,")
    print("su tasa de cambio es igual a cero.")
    print()
    print("Por lo tanto, en ese punto no hay crecimiento")
    print("ni disminución de la población.")
    print()
    print("Si la población comienza con 1500 ejemplares,")
    print("permanecerá en ese valor a medida que pasa el tiempo,")
    print("según el modelo matemático.")
    print()
    print("Por esta razón, 1500 ejemplares representa una")
    print("población de equilibrio.")
    print()
    print("Matemáticamente:")
    print("P(t) = 1.5")


# ------------------------------------------------------------
# 4.e) Ecuación diferencial anual a partir de la tasa trimestral
# ------------------------------------------------------------

def punto_4e():
    """
    Obtiene la ecuación diferencial anual a partir
    de la tasa de nacimientos y muertes trimestral.

    Nacimientos por trimestre = 150
    Muertes por trimestre = s

    Cambio neto trimestral:
        150 - s

    Como un año tiene 4 trimestres:
        dP/dt = 4(150 - s)

    Por lo tanto:
        dP/dt = 600 - 4s
    """

    print("4.e) Ecuación diferencial anual")
    print()
    print("Nacimientos por trimestre: 150")
    print("Muertes por trimestre: s")
    print()
    print("Cambio neto por trimestre:")
    print("150 - s")
    print()
    print("Como un año tiene cuatro trimestres:")
    print("dP/dt = 4(150 - s)")
    print()
    print("Ecuación diferencial anual:")
    print("dP/dt = 600 - 4s")


# ------------------------------------------------------------
# 4.f) Análisis del comportamiento de las soluciones
# ------------------------------------------------------------

def punto_4f():
    """
    Analiza el comportamiento de las soluciones considerando
    una tasa de muertes constante por trimestre.

    Si la cantidad de muertes no depende del tamaño de la
    población, la tasa de cambio también permanece constante.

    El comportamiento de la población depende de la relación
    entre nacimientos y muertes:
        - Si nacen más ejemplares de los que mueren,
          la población aumenta.
        - Si nacimientos y muertes se compensan,
          la población permanece constante.
        - Si mueren más ejemplares de los que nacen,
          la población disminuye.

    En este caso no aparece un punto de equilibrio que dependa
    del tamaño de la población. El comportamiento depende
    únicamente de la diferencia entre nacimientos y muertes.
    """

    print("4.f) Análisis del comportamiento de las soluciones")
    print()
    print("Si la cantidad de muertes por trimestre se mantiene")
    print("constante y no depende del tamaño de la población,")
    print("la tasa de cambio también permanece constante.")
    print()
    print("Por esta razón, la población tendrá un comportamiento")
    print("determinado por la diferencia entre nacimientos y muertes:")
    print()
    print("- Si los nacimientos superan las muertes,")
    print("  la población aumenta.")
    print()
    print("- Si los nacimientos y las muertes se compensan,")
    print("  la población permanece constante.")
    print()
    print("- Si las muertes superan los nacimientos,")
    print("  la población disminuye.")
    print()
    print("A diferencia del modelo logístico planteado anteriormente,")
    print("en este caso no aparece un punto de equilibrio que dependa")
    print("del tamaño de la población.")
    print()
    print("El comportamiento está determinado únicamente por")
    print("la diferencia entre nacimientos y muertes.")


# ============================================================
# EJECUTAR LOS PUNTOS 4.d, 4.e Y 4.f
# ============================================================

def punto_4():
    punto_4d()
    print("\n" + "=" * 60 + "\n")

    punto_4e()
    print("\n" + "=" * 60 + "\n")

    punto_4f()


# Ejecutar punto 4
if _name_ == "_main_":
    punto_4()