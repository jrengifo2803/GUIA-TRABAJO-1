# PUNTO 2 - DIAGRAMAS DE FASE
# ============================================================

def diagrama_fase(func, puntos_criticos, nombre, pruebas,
                  clasificaciones, ylim=None):
    """
    Dibuja el diagrama de fase de una ecuación autónoma y'=f(y).

    puntos_criticos: lista de puntos críticos.
    pruebas: lista de (valor_de_prueba, signo_o_resultado).
    """
    if ylim is None:
        minimo = min(puntos_criticos) - 2
        maximo = max(puntos_criticos) + 2
        ylim = (minimo, maximo)

    fig, ax = plt.subplots(figsize=(5, 8))

    # Línea vertical de fase.
    ax.plot([0, 0], ylim, color="black", linewidth=2)

    # Puntos críticos.
    for p in puntos_criticos:
        ax.scatter([0], [p], s=100, facecolors="white",
                   edgecolors="black", zorder=5)
        ax.text(0.12, p, f"y = {p:g}", va="center", fontsize=10)

    # Flechas por intervalo usando los valores de prueba.
    for valor, resultado in pruebas:
        signo = np.sign(resultado)
        if signo > 0:
            ax.annotate("", xy=(0, valor + 0.55), xytext=(0, valor - 0.55),
                        arrowprops=dict(arrowstyle="->", color="tab:blue",
                                        linewidth=2.5))
        else:
            ax.annotate("", xy=(0, valor - 0.55), xytext=(0, valor + 0.55),
                        arrowprops=dict(arrowstyle="->", color="tab:blue",
                                        linewidth=2.5))

    ax.set_xlim(-1, 1.7)
    ax.set_ylim(ylim)
    ax.set_xticks([])
    ax.set_ylabel("y")
    ax.set_title(nombre)
    ax.grid(alpha=0.2)

    texto = "\n".join(
        [f"y={p}: {clas}" for p, clas in zip(puntos_criticos, clasificaciones)]
    )
    ax.text(0.45, 0.02, texto, transform=ax.transAxes,
            va="bottom", fontsize=10,
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    plt.show()


def punto_2a():
    """
    2.a) y' = y(3-y)(y-2)
    Puntos críticos: 0, 2, 3
    """
    f = lambda y: y * (3-y) * (y-2)
    pruebas = [(-1, f(-1)), (1, f(1)), (2.5, f(2.5)), (4, f(4))]

    diagrama_fase(
        f,
        [0, 2, 3],
        "2.a) Diagrama de fase: y' = y(3-y)(y-2)",
        pruebas,
        ["estable", "inestable", "estable"],
        ylim=(-2, 5)
    )


def punto_2b():
    """
    2.b) y' = y^2 - y^3
    Puntos críticos: 0, 1
    """
    f = lambda y: y*2 - y*3
    pruebas = [(-1, f(-1)), (0.5, f(0.5)), (2, f(2))]

    diagrama_fase(
        f,
        [0, 1],
        "2.b) Diagrama de fase: y' = y² - y³",
        pruebas,
        ["semiestable", "estable"],
        ylim=(-2, 3)
    )


def punto_2c():
    """
    2.c) y' = (y+2)(10+3y-y^2)
    Puntos críticos: -2, 5
    """
    f = lambda y: (y+2) * (10 + 3*y - y**2)
    pruebas = [(-3, f(-3)), (0, f(0)), (6, f(6))]

    diagrama_fase(
        f,
        [-2, 5],
        "2.c) Diagrama de fase: y' = (y+2)(10+3y-y²)",
        pruebas,
        ["semiestable", "estable"],
        ylim=(-4, 7)
    )


def punto_2d():
    """
    2.d) y' = y^5 - 4y^3 - 5y^2

    Puntos críticos reales:
        y=0
        y≈2.457
    """
    f = lambda y: y*5 - 4*y3 - 5*y*2

    # Única raíz real distinta de 0 de y^3 - 4y - 5 = 0.
    raiz = np.roots([1, 0, -4, -5])
    raiz_real = float(np.real(raiz[np.isclose(np.imag(raiz), 0)][0]))

    pruebas = [(-1, f(-1)), (1, f(1)), (3, f(3))]

    diagrama_fase(
        f,
        [0, raiz_real],
        "2.d) Diagrama de fase: y' = y⁵ - 4y³ - 5y²",
        pruebas,
        ["semiestable", "inestable"],
        ylim=(-2, 5)
    )

    print(f"Raíz real adicional de y³ - 4y - 5 = {raiz_real:.6f}")


def punto_2e():
    """
    2.e) y' = (1-y)(y-2)^3
    Puntos críticos: 1, 2
    """
    f = lambda y: (1-y) * (y-2)**3
    pruebas = [(0, f(0)), (1.5, f(1.5)), (3, f(3))]

    diagrama_fase(
        f,
        [1, 2],
        "2.e) Diagrama de fase: y' = (1-y)(y-2)³",
        pruebas,
        ["inestable", "estable"],
        ylim=(-1, 4)
    )


def punto_2():
    """Ejecuta todos los ejercicios del punto 2."""
    punto_2a()
    punto_2b()
    punto_2c()
    punto_2d()
    punto_2e()


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def main():
    print("\nTALLER 1 - ECUACIONES DIFERENCIALES")
    print("------------------------------------")
    print("1  -> Ejecutar todo el punto 1")
    print("2  -> Ejecutar todo el punto 2")
    print("3  -> Ejecutar todo el taller")
    print("0  -> Salir")

    opcion = input("\nSelecciona una opción: ").strip()

    if opcion == "1":
        punto_1()
    elif opcion == "2":
        punto_2()
    elif opcion == "3":
        punto_1()
        punto_2()
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")


if _name_ == "_main_":
    main()