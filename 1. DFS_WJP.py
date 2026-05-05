from collections import deque

def water_jug_problem(x, y, z):
    visited = set()
    queue = deque([(0, 0)])  # initial state (0,0)

    while queue:
        a, b = queue.popleft()

        # If we reach the target
        if a == z or b == z:
            print("Solution found:", (a, b))
            return True

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Possible moves
        queue.append((x, b))  # Fill jug X
        queue.append((a, y))  # Fill jug Y
        queue.append((0, b))  # Empty jug X
        queue.append((a, 0))  # Empty jug Y

        # Pour X -> Y
        pour = min(a, y - b)
        queue.append((a - pour, b + pour))

        # Pour Y -> X
        pour = min(b, x - a)
        queue.append((a + pour, b - pour))

    print("No solution possible")
    return False


# Example
x = 4   # capacity of jug X
y = 3   # capacity of jug Y
z = 2   # target

water_jug_problem(x, y, z)
