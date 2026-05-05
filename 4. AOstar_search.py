# AO* Algorithm implementation

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],  # OR between [(B AND C)] or [D]
    'B': [[('E', 1)], [('F', 1)]],
    'C': [[('G', 1)]],
    'D': [[('H', 1)]],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Initial heuristic values
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0
}

# To store solution graph
solution = {}

def ao_star(node):
    if not graph[node]:  # terminal node
        return heuristic[node]

    min_cost = float('inf')
    best_option = None

    # Each option represents AND nodes
    for option in graph[node]:
        cost = 0
        for child, weight in option:
            cost += ao_star(child) + weight

        if cost < min_cost:
            min_cost = cost
            best_option = option

    heuristic[node] = min_cost
    solution[node] = best_option

    return min_cost


# Run AO*
start = 'A'
cost = ao_star(start)

# Print solution
def print_solution(node):
    if node not in solution:
        return
    print(f"{node} -> {solution[node]}")
    for child, _ in solution[node]:
        print_solution(child)

print("Minimum Cost:", cost)
print("Solution Graph:")
print_solution(start)
