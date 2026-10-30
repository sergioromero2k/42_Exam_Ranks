def count_islands(grid: list[str]) -> int:
    if not grid:
        return 0

    visited = set()
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#' and (r, c) not in visited:
                count += 1
                pending = [(r, c)]
                visited.add((r, c))

                while pending:
                    x, y = pending.pop()

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            if grid[nx][ny] == '#' and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                pending.append((nx, ny))

    return count
