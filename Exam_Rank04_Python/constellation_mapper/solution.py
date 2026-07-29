def constellation_mapper(stars: list[tuple[int, int]], size: int):
    grid = [["." for _ in range(size)] for _ in range(size)]
    for r, c in stars:
        if 0 <= r < size and 0 <= c < size:
            grid[r][c] = "*"
    return [["".join(row)] for row in grid]
