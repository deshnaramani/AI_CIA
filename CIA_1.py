from flask import Flask, render_template, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt
import heapq

app = Flask(__name__)

# Helper function: create graph from user input
def create_graph(vertices, edges):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    for edge in edges:
        u, v, weight = edge
        G.add_edge(u, v, weight=int(weight))
    return G

# Algorithm: British Museum Search (BMS)
def british_museum_search(G, start, goal):
    paths = []
    def dfs(v, path=[]):
        if v == goal:
            paths.append(path + [v])
        for neighbor in G.neighbors(v):
            if neighbor not in path:
                dfs(neighbor, path + [v])
    dfs(start)
    return paths

# Algorithm: Depth-First Search (DFS)
def dfs_search(G, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in G[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))
    return []

# Algorithm: Breadth-First Search (BFS)
def bfs_search(G, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in G[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return []

# Algorithm: Hill Climbing Search
def hill_climbing_search(G, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == goal:
            return path
        visited.add(vertex)
        neighbors = sorted(list(G.neighbors(vertex)))  # Heuristic ordering (lexicographic)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return []

# Algorithm: Beam Search
def beam_search(graph, start, goal, beam_width):
    queue = [[start]]
    while queue:
        next_queue = []
        for path in queue:
            node = path[-1]
            if node == goal:
                return path
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = path + [neighbor]
                next_queue.append(new_path)
        queue = sorted(next_queue, key=lambda p: p[-1])[:beam_width]
    return None

# Algorithm: Branch and Bound
def branch_and_bound(graph, start, goal, costs):
    best_path = None
    best_cost = float('inf')
    
    def bnb(vertex, path, cost):
        nonlocal best_path, best_cost
        if vertex == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path[:]
            return
        
        for neighbor in graph[vertex]:
            if neighbor not in path:
                path.append(neighbor)
                bnb(neighbor, path, cost + costs[neighbor])
                path.pop()

    bnb(start, [start], 0)
    return best_path

# Algorithm: Branch and Bound + Extended Lists
def branch_and_bound_extended(graph, start, goal, costs):
    visited = set()
    best_path = []
    best_cost = float('inf')

    def bnb_extended(vertex, path, cost):
        nonlocal best_path, best_cost
        if vertex == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path[:]
            return

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                bnb_extended(neighbor, path, cost + costs[neighbor])
                path.pop()
                visited.remove(neighbor)

    bnb_extended(start, [start], 0)
    return best_path

# Algorithm: Branch and Bound with Heuristics
def branch_and_bound_with_heuristics(graph, start, goal, costs, heuristic):
    best_path = []
    best_cost = float('inf')

    def bnb_with_h(vertex, path, cost):
        nonlocal best_path, best_cost
        if vertex == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path[:]
            return

        for neighbor in graph[vertex]:
            if neighbor not in path:
                new_cost = cost + costs[neighbor] + heuristic[neighbor]
                if new_cost < best_cost:
                    path.append(neighbor)
                    bnb_with_h(neighbor, path, cost + costs[neighbor])
                    path.pop()

    bnb_with_h(start, [start], 0)
    return best_path

# Algorithm: A*
def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start, [start]))
    closed_set = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in closed_set:
                new_path = path + [neighbor]
                cost = len(new_path) + heuristic[neighbor]
                heapq.heappush(open_set, (cost, neighbor, new_path))

    return None

# Algorithm: AO*
def ao_star(graph, start, goal):
    # AO* implementation - finding the best path considering AND/OR relationships
    def recursive_ao(vertex):
        if vertex == goal:
            return [vertex]
        best_path = None
        for neighbor in graph[vertex]:
            path = recursive_ao(neighbor)
            if path:
                current_path = [vertex] + path
                if best_path is None or len(current_path) < len(best_path):
                    best_path = current_path
        return best_path

    return recursive_ao(start)

# Algorithm: Best-First Search
def best_first_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start, [start]))
    closed_set = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in closed_set:
                new_path = path + [neighbor]
                cost = heuristic[neighbor]
                heapq.heappush(open_set, (cost, neighbor, new_path))

    return None

# Algorithm: Oracle
def oracle(graph, start, goal, heuristic):
    """
    A simple heuristic-based search that prioritizes nodes based on heuristic values.
    This implementation can be viewed as a variation of the best-first search.
    """
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start, [start]))
    closed_set = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in closed_set:
                new_path = path + [neighbor]
                cost = len(new_path) + heuristic[neighbor]
                heapq.heappush(open_set, (cost, neighbor, new_path))

    return None

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    vertices = request.json['vertices']
    edges = request.json['edges']
    algorithm = request.json['algorithm']
    start = request.json['start']
    goal = request.json['goal']

    G = create_graph(vertices, edges)

    # Initialize heuristic for algorithms
    heuristic = {v: 1 for v in vertices}  # Replace with actual heuristic values if needed
    costs = {v: 1 for v in vertices}       # Replace with actual costs if needed

    # Select algorithm based on user input
    if algorithm == 'bms':
        paths = british_museum_search(G, start, goal)
    elif algorithm == 'dfs':
        paths = dfs_search(G, start, goal)
    elif algorithm == 'bfs':
        paths = bfs_search(G, start, goal)
    elif algorithm == 'hill_climbing':
        paths = hill_climbing_search(G, start, goal)
    elif algorithm == 'beam_search':
        paths = beam_search(G, start, goal, beam_width=2)  # Example beam width
    elif algorithm == 'branch_and_bound':
        paths = branch_and_bound(G, start, goal, costs)
    elif algorithm == 'oracle':
        paths = oracle(G, start, goal, heuristic)
    elif algorithm == 'best_first':
        paths = best_first_search(G, start, goal, heuristic)
    elif algorithm == 'a_star':
        paths = a_star_search(G, start, goal, heuristic)
    elif algorithm == 'ao_star':
        paths = ao_star(G, start, goal)
    else:
        return jsonify({"error": "Algorithm not implemented yet."})

    # Generate initial and final graph images
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12)
    plt.savefig('static/initial_graph.png')
    plt.close()

    return jsonify({'path': paths})

if __name__ == '__main__':
    app.run(debug=True)
