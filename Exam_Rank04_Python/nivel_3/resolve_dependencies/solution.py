

# ALGORITMO: Kahn's Algorithm (Topological Sort con BFS)
# def package_dependency_solver(packages: dict[str, list[str]]) -> list[str]:
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    deps = {p: {d for d in ds if d in packages} for p, ds in packages.items()}
    order = []
    while deps:
        ready = sorted(p for p, ds in deps.items() if not ds)
        if not ready:
            return []
        order += ready
        for p in ready:
            del deps[p]
        for ds in deps.values():
            ds.difference_update(ready)
    return order
