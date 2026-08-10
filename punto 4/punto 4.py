import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE DIRECTORIOS
# ============================================================
# Se crea la carpeta 'graficas' si no existe para almacenar los previews.
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"
CARPETA_GRAFICAS.mkdir(exist_ok=True)

# ============================================================
# FUNCIONES MATEMÁTICAS
# ============================================================
def dPdt(t, P):
    """Ecuación diferencial original: dP/dt = 3P - 2P^2"""
    return 3*P - 2*P**2

# ============================================================
# GENERACIÓN DE GRÁFICAS
# ============================================================
def graficar_diagrama_fase_y_soluciones():
    """Genera el diagrama de fase y las soluciones para P(0)=2 y P(0)=0.1"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # 1. Crear el Campo de Pendientes
    t_vals = np.linspace(0, 5, 25)
    P_vals = np.linspace(-0.2, 2.5, 25)
    T, P_grid = np.meshgrid(t_vals, P_vals)
    
    U = np.ones_like(T)
    V = dPdt(T, P_grid)
    
    # Normalización del campo vectorial
    N = np.sqrt(U**2 + V**2)
    N[N == 0] = 1 
    U, V = U / N, V / N
    
    ax.quiver(T, P_grid, U, V, color='lightgray', angles='xy', pivot='mid', label='Campo de pendientes')

    # 2. Puntos Críticos (Equilibrio)
    ax.axhline(1.5, color='green', linestyle='--', linewidth=2.5, label='P = 1.5 (Estable / Capacidad)')
    ax.axhline(0, color='red', linestyle='--', linewidth=2.5, label='P = 0 (Inestable)')

    # 3. Resolver y graficar las condiciones iniciales
    t_eval = np.linspace(0, 5, 200)

    # Población inicial de 2000 (P=2.0)
    sol_b = solve_ivp(dPdt, [0, 5], [2.0], t_eval=t_eval)
    ax.plot(sol_b.t, sol_b.y[0], 'b-', linewidth=3, label='P(0) = 2.0 (Decrece hacia 1.5)')

    # Población inicial de 100 (P=0.1)
    sol_c = solve_ivp(dPdt, [0, 5], [0.1], t_eval=t_eval)
    ax.plot(sol_c.t, sol_c.y[0], 'm-', linewidth=3, label='P(0) = 0.1 (Crece hacia 1.5)')

    # 4. Ajustes estéticos y exportación
    ax.scatter([0, 0], [2.0, 0.1], color='black', zorder=5)
    ax.set_title('Diagrama de Fase y Soluciones: dP/dt = 3P - 2P²', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tiempo (años)', fontsize=12)
    ax.set_ylabel('Población P (en miles)', fontsize=12)
    ax.set_ylim(-0.2, 2.5)
    ax.set_xlim(0, 5)
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='upper right', fontsize=10, shadow=True)
    plt.tight_layout()

    # Guardar gráfica para el README
    ruta_fase = CARPETA_GRAFICAS / "4_diagrama_fases_poblacion.png"
    plt.savefig(ruta_fase, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"✓ Gráfica creada: {ruta_fase}")

def graficar_comportamiento_segun_s():
    """Genera la gráfica de los puntos de equilibrio dependiendo de la tasa de muertes 's'"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Valores de s desde 0 hasta el discriminante cero (431.25)
    s_vals = np.linspace(0, 431.25, 500)
    
    # Ecuación cuadrática para los equilibrios: P = (3 ± sqrt(13.8 - 0.032s)) / 4
    discriminante = 13.8 - 0.032 * s_vals
    P_estable = (3 + np.sqrt(discriminante)) / 4
    P_inestable = (3 - np.sqrt(discriminante)) / 4

    ax.plot(s_vals, P_estable, 'g-', linewidth=2.5, label='Equilibrio Estable (Superior)')
    ax.plot(s_vals, P_inestable, 'r--', linewidth=2.5, label='Equilibrio Inestable (Umbral)')
    
    # Marcar el punto donde el discriminante es 0 (s = 431.25)
    ax.axvline(431.25, color='black', linestyle=':', label='s = 431.25 (Punto de bifurcación)')
    ax.scatter([431.25], [0.75], color='black', zorder=5)
    ax.annotate('P = 0.75\ns = 431.25', xy=(431.25, 0.75), xytext=(350, 0.5),
                arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Ajustes estéticos y exportación
    ax.set_title('Puntos de equilibrio según la tasa de muertes (s)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tasa de muertes por trimestre (s)', fontsize=12)
    ax.set_ylabel('Población de equilibrio P (en miles)', fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='lower left', fontsize=10, shadow=True)
    plt.tight_layout()

    # Guardar gráfica para el README
    ruta_s = CARPETA_GRAFICAS / "4f_comportamiento_segun_s.png"
    plt.savefig(ruta_s, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"✓ Gráfica creada: {ruta_s}")


# ============================================================
# REPORTES DE ANÁLISIS EN CONSOLA
# ============================================================
def imprimir_analisis():
    reporte = """
======================================================================
TALLER 1 - PUNTO 4: MODELO POBLACIONAL
======================================================================
a) Puntos críticos de dP/dt = 3P - 2P²:
   P = 0 (Inestable) y P = 1.5 (Estable, Capacidad de carga).

b) Población inicial de 2000 (P=2.0):
   Al ser mayor que 1.5, la población decrece asintóticamente hacia 1.5.

c) Población inicial de 100 (P=0.1):
   Al estar entre 0 y 1.5, la población crece continuamente hacia 1.5.

d) Población de 1500 (P=1.5):
   Al ser un punto crítico (dP/dt = 0), la población permanece constante.

e) Ecuación anual considerando nacimientos y muertes (s):
   dP/dt = 3P - 2P² + 0.6 - 0.004s

f) Comportamiento según s:
   La existencia de equilibrios depende de las raíces de la ecuación.
   Si s > 431.25, no existen puntos críticos reales y la especie se extingue.
======================================================================
    """
    print(reporte)


# ==========================================
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# ==========================================
def main():
    imprimir_analisis()
    print("Generando gráficas para el README...")
    graficar_diagrama_fase_y_soluciones()
    graficar_comportamiento_segun_s()
    print("\n¡Proceso finalizado con éxito!")

if __name__ == '__main__':
    main()


# Ejecutar punto 4
if _name_ == "_main_":
    punto_4()
