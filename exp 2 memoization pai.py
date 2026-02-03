def memo_water_jug(jug1, jug2, target, a=0, b=0, memo=None):
    if memo is None:
        memo = {}
    if (a, b) in memo:
        return memo[(a, b)]
    print(a, b)
    if a == target or b == target:
        print("Reached target!")
        memo[(a, b)] = True
        return True
    memo[(a, b)] = False
    moves = [
        (jug1, b),
        (a, jug2),
        (0, b),
        (a, 0),
        (a - min(a, jug2 - b), b + min(a, jug2 - b)),
        (a + min(b, jug1 - a), b - min(b, jug1 - a))
    ]
    for move in moves:
        if memo_water_jug(jug1, jug2, target, move[0], move[1], memo):
            memo[(a, b)] = True
            return True
    return memo[(a, b)]
