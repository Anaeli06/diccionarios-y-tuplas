hechos = {
    ("juan", "padre", "carlos"),
    ("juan", "padre", "ana"),
    ("carlos", "padre", "luis"),
    ("carlos", "padre", "sofia"),
    ("luis", "padre", "mateo"),
}


def consultar(sujeto=None, predicado=None, objeto=None):
    """Devuelve los hechos que coinciden con los campos especificados.

    None funciona como comodín.
    """
    return sorted(
        (s, p, o)
        for s, p, o in hechos
        if (sujeto is None or sujeto == s)
        and (predicado is None or predicado == p)
        and (objeto is None or objeto == o)
    )


def obtener_pares_padre():
    """Obtiene las parejas (padre, hijo) a partir de los hechos."""
    return {(s, o) for s, p, o in hechos if p == "padre"}


def inferir_hijos():
    """R1: padre(X, Y) -> hijo(Y, X). Devuelve (hijo, padre)."""
    return {(hijo, padre) for padre, hijo in obtener_pares_padre()}


def inferir_abuelos():
    """R2: padre(X, Y) y padre(Y, Z) -> abuelo(X, Z)."""
    pares = obtener_pares_padre()
    return {
        (abuelo, nieto)
        for abuelo, padre in pares
        for padre2, nieto in pares
        if padre == padre2
    }


def inferir_hermanos():
    """R3: padre(Z, X) y padre(Z, Y) y X != Y -> hermano(X, Y)."""
    pares = obtener_pares_padre()
    return {
        (persona_a, persona_b)
        for padre_a, persona_a in pares
        for padre_b, persona_b in pares
        if padre_a == padre_b and persona_a != persona_b
    }


def inferir_ancestros():
    """R4 recursiva: padre(X,Y) -> ancestro(X,Y);
    ancestro(X,Y) y padre(Y,Z) -> ancestro(X,Z).
    """
    pares = obtener_pares_padre()
    ancestros = set(pares)
    cambio = True

    while cambio:
        cambio = False
        nuevos = {
            (ancestro, descendiente)
            for ancestro, intermediario in ancestros
            for padre, descendiente in pares
            if intermediario == padre
        }
        nuevos -= ancestros
        if nuevos:
            ancestros.update(nuevos)
            cambio = True

    return ancestros


if __name__ == "__main__":
    print("HECHOS REGISTRADOS")
    for hecho in sorted(hechos):
        print(f"{hecho[1]}({hecho[0]}, {hecho[2]})")

    print("\\nCONSULTA: hijos de Carlos")
    print(consultar(sujeto="carlos", predicado="padre"))

    print("\\nRELACIONES INFERIDAS")
    print("Hijo (hijo, padre):", sorted(inferir_hijos()))
    print("Abuelo (abuelo, nieto):", sorted(inferir_abuelos()))
    print("Hermano (persona, hermano):", sorted(inferir_hermanos()))
    print("Ancestro (ancestro, descendiente):", sorted(inferir_ancestros()))

    print("\\nPREGUNTAS DE PRUEBA")
    print("¿Juan es abuelo de Luis?", ("juan", "luis") in inferir_abuelos())
    print("¿Luis y Sofía son hermanos?", ("luis", "sofia") in inferir_hermanos())
