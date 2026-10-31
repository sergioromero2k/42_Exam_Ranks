"""Dibujar estrellas * en una cuadrícula según unas coordenadas, ignorando las que estén fuera de los límites."""


def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    return ["".join("*" if (r, c) in stars else "." for c in range(dim)) for r in range(dim)]
