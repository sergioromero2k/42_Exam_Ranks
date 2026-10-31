def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    return ["".join("*" if (r, c) in stars else "." for c in range(dim)) for c in range(dim)]
