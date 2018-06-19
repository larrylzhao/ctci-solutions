def path_through_grid(grid):
    if len(grid) == 0:
        return []
    search = []
    for r, row in enumerate(grid):
        search.append([])
        for c, blocked in enumerate(row):
            if r == 0 and c == 0:
                search[r].append("start")
            elif blocked:
                search[r].append(None)
            elif r > 0 and search[r-1][c]:
                search[r].append("down")
            elif c > 0 and search[r][c-1]:
                search[r].append("right")
            else:
                search[r].append(None)
        path = ["end"]
        r, c = len(grid) - 1, len(grid[0]) - 1
        if not search[r][c]:
            return None
        while c > 0 or r > 0:
            path.append(search[r][c])
