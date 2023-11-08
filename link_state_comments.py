# Define the graph using a function that returns a dictionary of nodes and their neighbors with edge weights.
def initial_graph():
    return {
        'A': {'B': 1, 'C': 4, 'D': 2},
        'B': {'A': 9, 'E': 5},
        'C': {'A': 4, 'F': 15},
        'D': {'A': 10, 'F': 7},
        'E': {'B': 3, 'J': 7},
        'F': {'C': 11, 'D': 14, 'K': 3, 'G': 9},
        'G': {'F': 12, 'I': 4},
        'H': {'J': 13},
        'I': {'G': 6, 'J': 7},
        'J': {'H': 2, 'I': 4},
        'K': {'F': 6}
    }

# Initialize the starting node for finding the shortest path.
initial = 'A'

# Create dictionaries to store path distances, previous nodes, a queue of nodes to process, and the graph itself.
path = {}
adj_node = {}
queue = []
graph = initial_graph()

# Initialize path distances, previous nodes, and add all nodes to the queue.
for node in graph:
    path[node] = float("inf")  # Initialize path distances to infinity.
    adj_node[node] = None  # Initialize previous nodes as None.
    queue.append(node)

# Set the distance of the initial node to 0.
path[initial] = 0

# Main loop to find the shortest path using Dijkstra's algorithm.
while queue:
    # Find the node with the minimum path distance that has not been marked as visited.
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)

    # Explore neighbors of the current node.
    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        # Update path if a shorter path is found.
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur

# Prompt the user to enter the ending node.
x = str(input("Enter the ending node: "))

# Display the path from the initial node 'A' to the user-specified ending node.
print('The path between A to', x)
path_to_x = [x]

# Reconstruct and reverse the path from the ending node to 'A'.
while adj_node[x] is not None:
    x = adj_node[x]
    path_to_x.append(x)
path_to_x.reverse()

# Print the path in the correct order.
print(' -> '.join(path_to_x))
