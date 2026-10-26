# Xom Data · Number of islands
# Problem: https://xomdata.com/practice/py-count-islands
# Solved: 2026-10-26

def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 1 or (row, col) in visited:
                continue

            islands += 1
            stack = [(row, col)]
            visited.add((row, col))

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

    return islands
