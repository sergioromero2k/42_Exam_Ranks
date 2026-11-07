

# ALGORITMO: Kahn's Algorithm (Topological Sort con BFS)
# def package_dependency_solver(packages: dict[str, list[str]]) -> list[str]:
"""Tienes que decir en qué orden instalar unos programas, sabiendo que algunos necesitan que otro esté instalado antes."""


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    instalados = []
    while len(instalados) < len(packages):
        listos = sorted(
            paquete
            for paquete in packages
            if paquete not in instalados
            and all(dependencia in instalados or dependencia not in packages
                    for dependencia in packages[paquete])
        )
        if not listos:
            return []
        instalados += listos
    return instalados

print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
print(package_dependency_resolver({"A": ["B"], "B": ["A"]}))