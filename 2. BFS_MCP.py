from collections import deque

# Check if state is valid
def is_valid(m, c):
    # missionaries and cannibals must be within bounds
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # missionaries should not be outnumbered
    if (m > 0 and c > m):
        return False
    # check right side also
    m_right = 3 - m
    c_right = 3 - c
    if (m_right > 0 and c_right > m_right):
        return False
    return True

# BFS function
def missionaries_cannibals():
    start = (3, 3, 1)  # all on left, boat on left
    goal = (0, 0, 0)   # all on right

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) in visited:
            continue
        visited.add((m, c, boat))

        # Goal reached
        if (m, c, boat) == goal:
            return path + [(m, c, boat)]

        # Possible moves
        moves = [
            (1, 0), (2, 0),  # 1 or 2 missionaries
            (0, 1), (0, 2),  # 1 or 2 cannibals
            (1, 1)           # 1 missionary and 1 cannibal
        ]

        for dm, dc in moves:
            if boat == 1:  # boat on left → go right
                new_state = (m - dm, c - dc, 0)
            else:          # boat on right → go left
                new_state = (m + dm, c + dc, 1)

            if is_valid(*new_state[:2]):
                queue.append((new_state, path + [(m, c, boat)]))

    return None

# Run the program
solution = missionaries_cannibals()

# Print solution
if solution:
    print("Solution steps:\n")
    for step in solution:
        print(step)
else:
    print("No solution found")
