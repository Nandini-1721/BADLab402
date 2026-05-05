import heapq

# A* Algorithm
def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f, node)

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None


# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0
}

# Run A*
start = 'A'
goal = 'F'

path = a_star(graph, start, goal, heuristic)

print("Shortest Path:", path)
