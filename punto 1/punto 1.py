
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ============================================================
# FUNCIONES GENERALES
# ============================================================

def campo_pendientes(f, xlim=(-5, 5), ylim=(-5, 5), nx=25, ny=25,
                     ax=None, color="gray"):
    """Dibuja el campo de pendientes y' = f(x,y)."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 6))

    x = np.linspace(xlim[0], xlim[1], nx)
    y = np.linspace(ylim[0], ylim[1], ny)
    X, Y = np.meshgrid(x, y)

    M = f(X, Y)

    # Segmentos de longitud similar.
    U = np.ones_like(M)
    V = M
    norma = np.sqrt(U*2 + V*2)
    U = U / norma
    V = V / norma

    ax.quiver(X, Y, U, V, color=color, alpha=0.55,
              pivot="mid", angles="xy", width=0.0025)
    ax.axhline(0, color="black", linewidth=0.7)
    ax.axvline(0, color="black", linewidth=0.7)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(alpha=0.2)

    return ax


def dibujar_familia(ax, soluciones, x, labels=None):
    """Dibuja varias soluciones de una familia."""
    for i, y in enumerate(soluciones):
        label = labels[i] if labels else None
        ax.plot(x, y, linewidth=1.5, alpha=0.65, label=label)


# ============================================================
# PUNTO 1
# ============================================================

def punto_1a():
    """
    1.a) y' = -y - sin(x), y(0)=1

    Solución particular:
        y = (cos(x) - sin(x) + exp(-x))/2

    Familia:
        y = (cos(x) - sin(x))/2 + C exp(-x)
    """
    f = lambda x, y: -y - np.sin(x)
    x = np.linspace(-5, 5, 700)

    ax = campo_pendientes(f, (-5, 5), (-2, 3))

    # Familia de soluciones.
    for C in [-1.0, -0.5, 0, 0.5, 1.0]:
        y = (np.cos(x) - np.sin(x)) / 2 + C * np.exp(-x)
        ax.plot(x, y, alpha=0.55)

    # Solución particular C = 1/2.
    y_part = (np.cos(x) - np.sin(x) + np.exp(-x)) / 2
    ax.plot(x, y_part, "r", linewidth=2.5, label="Solución particular")
    ax.scatter([0], [1], color="blue", zorder=5, label="(0,1)")

    ax.set_title("1.a) Campo de pendientes y solución particular")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1b():
    """
    1.b) y' = x + y, y(-2)=2

    Familia:
        y = C exp(x) - x - 1

    Particular:
        y = exp(x+2) - x - 1
    """
    f = lambda x, y: x + y
    x = np.linspace(-5, 2.5, 700)

    ax = campo_pendientes(f, (-5, 2.5), (-5, 10))

    for C in [-2, -1, 0, 1, 2]:
        y = C * np.exp(x) - x - 1
        ax.plot(x, y, alpha=0.55)

    y_part = np.exp(x + 2) - x - 1
    ax.plot(x, y_part, "r", linewidth=2.5, label="Solución particular")
    ax.scatter([-2], [2], color="blue", zorder=5, label="(-2,2)")

    ax.set_title("1.b) Campo de pendientes y solución particular")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1c():
    """
    1.c) y' = -x^2 + sin(y)

    No se da condición inicial en la guía.
    Se elige y(0)=0.

    La solución particular se obtiene numéricamente.
    """
    f = lambda x, y: -x**2 + np.sin(y)

    # Integramos hacia izquierda y derecha desde (0,0).
    x_left = np.linspace(-3, 0, 400)
    x_right = np.linspace(0, 3, 400)

    sol_left = solve_ivp(lambda x, y: f(x, y), (0, -3), [0],
                         dense_output=True, max_step=0.02)
    sol_right = solve_ivp(lambda x, y: f(x, y), (0, 3), [0],
                          dense_output=True, max_step=0.02)

    ax = campo_pendientes(f, (-3, 3), (-4, 4))

    ax.plot(x_left, sol_left.sol(x_left)[0], "r", linewidth=2.5)
    ax.plot(x_right, sol_right.sol(x_right)[0], "r", linewidth=2.5,
            label="Solución particular, y(0)=0")
    ax.scatter([0], [0], color="blue", zorder=5, label="(0,0)")

    ax.set_title("1.c) Campo de pendientes y solución numérica")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1d():
    """
    1.d) (x^2+1)y' + 3xy = 6x

    Despejada:
        y' = (6x - 3xy)/(x^2+1)

    Se elige y(0)=1.

    Familia:
        y = 2 + C/(x^2+1)^(3/2)

    Particular:
        y = 2 - 1/(x^2+1)^(3/2)
    """
    f = lambda x, y: (6*x - 3*x*y) / (x**2 + 1)
    x = np.linspace(-4, 4, 700)

    ax = campo_pendientes(f, (-4, 4), (-1, 4))

    for C in [-2, -1, 0, 1, 2]:
        y = 2 + C / (x*2 + 1)*1.5
        ax.plot(x, y, alpha=0.55)

    y_part = 2 - 1 / (x*2 + 1)*1.5
    ax.plot(x, y_part, "r", linewidth=2.5, label="Solución particular")
    ax.scatter([0], [1], color="blue", zorder=5, label="(0,1)")

    ax.set_title("1.d) Campo de pendientes y solución particular")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1e():
    """
    1.e) y' = x exp(y)

    Se elige y(0)=0.

    Familia:
        y = -ln(C - x^2/2)

    Particular:
        y = -ln(1 - x^2/2)

    Dominio de la particular:
        |x| < sqrt(2)
    """
    f = lambda x, y: x * np.exp(y)

    # Para la particular se respeta su dominio real.
    eps = 1e-3
    xmax = np.sqrt(2) - eps
    x = np.linspace(-xmax, xmax, 700)

    ax = campo_pendientes(f, (-2, 2), (-2, 5))

    # Algunas curvas de la familia, solo donde el logaritmo está definido.
    for C in [0.75, 1.0, 1.5, 2.0]:
        inside = C - x**2 / 2
        mask = inside > 0
        y = np.full_like(x, np.nan)
        y[mask] = -np.log(inside[mask])
        ax.plot(x, y, alpha=0.55)

    y_part = -np.log(1 - x**2 / 2)
    ax.plot(x, y_part, "r", linewidth=2.5, label="Solución particular")
    ax.scatter([0], [0], color="blue", zorder=5, label="(0,0)")

    ax.set_title("1.e) Campo de pendientes y solución particular")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1f():
    """
    1.f) y' = x - y, y(1)=1

    Familia:
        y = x - 1 + C exp(-x)

    Particular:
        y = x - 1 + exp(1-x)
    """
    f = lambda x, y: x - y
    x = np.linspace(-4, 4, 700)

    ax = campo_pendientes(f, (-4, 4), (-4, 5))

    for C in [-2, -1, 0, 1, 2]:
        y = x - 1 + C * np.exp(-x)
        ax.plot(x, y, alpha=0.55)

    y_part = x - 1 + np.exp(1 - x)
    ax.plot(x, y_part, "r", linewidth=2.5, label="Solución particular")
    ax.scatter([1], [1], color="blue", zorder=5, label="(1,1)")

    ax.set_title("1.f) Campo de pendientes y solución particular")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


def punto_1():
    """Ejecuta todos los ejercicios del punto 1."""
    punto_1a()
    punto_1b()
    punto_1c()
    punto_1d()
    punto_1e()
    punto_1f()

    main()
# ============================================================