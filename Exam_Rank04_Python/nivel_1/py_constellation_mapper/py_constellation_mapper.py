"""Dibujar estrellas * en una cuadrícula según unas coordenadas, ignorando las que estén fuera de los límites."""


def constellation_mapper(stars: list[tuple[int, int]], size: int):
    grid = [["." for _ in range(size)] for _ in range(size)]
    for r, c in stars:
        if 0 <= r < size and 0 <= c < size:
            grid[r][c] = "*"
    return [["".join(row)] for row in grid]
