import heapq

# ALGORITMO: Kahn's Algorithm (Topological Sort con BFS)
def resolve_dependencies(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    valid = set(packages)
    skip = {p for p, d in packages.items() if any(x not in valid for x in d)}
    prev = None
    while prev != skip:
        prev = skip.copy()
        skip |= {p for p, d in packages.items() if p not in skip and any(x in skip for x in d)}

    nodes = valid - skip
    in_degree = {n: 0 for n in nodes}
    adj = {n: [] for n in nodes}
    for p in nodes:
        for dep in packages[p]:
            adj[dep].append(p)
            in_degree[p] += 1

    heap = [n for n in nodes if in_degree[n] == 0]
    heapq.heapify(heap)
    result = []
    while heap:
        curr = heapq.heappop(heap)
        result.append(curr)
        for dep in adj[curr]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                heapq.heappush(heap, dep)

    return result if len(result) == len(nodes) else []