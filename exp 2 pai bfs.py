from collections import deque
def bfs_water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)]) 
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
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
            if move not in visited:
                queue.append(move)
    return False
