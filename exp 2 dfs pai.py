def dfs_water_jug(jug1, jug2, target, a=0, b=0, visited=None):
    if visited is None:
        visited = set()
    if (a, b) in visited:
        return False
    visited.add((a, b))
    print(a, b)
    if a == target or b == target:
        print("Reached target!")
        return True
    moves = [
        (jug1, b),
        (a, jug2),
        (0, b),
        (a, 0),
        (a - min(a, jug2 - b), b + min(a, jug2 - b)),
        (a + min(b, jug1 - a), b - min(b, jug1 - a))
    ]
    for move in moves:
        if dfs_water_jug(jug1, jug2, target, move[0], move[1], visited):
            return True
    return False
