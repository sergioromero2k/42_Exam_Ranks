def constellation_mapper(coordinates, size):
    grid = [["." for _ in range(size)] for _ in range(size)]
    for r, c in coordinates:
        if 0 <= r < size and 0 <= c < size:
            grid[r][c] = "*"
    return [["".join(row)] for row in grid]