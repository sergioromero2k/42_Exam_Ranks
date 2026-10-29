"""
Dibujar una cuadrícula con bordes usando # y el interior con ..
"""


def grid_border(rows: int, cols: int) -> list[str]:
    grid: list[str] = []

    if cols <= 0 or rows <= 0:
        return grid
    for r in range(rows):
        curr_line: str = ""
        for c in range(cols):
            if (r == 0 or r == (rows - 1)
                    or c == 0 or c == (cols - 1)):
                curr_line += "#"
            else:
                curr_line += "."
        grid.append(curr_line)
    return grid
