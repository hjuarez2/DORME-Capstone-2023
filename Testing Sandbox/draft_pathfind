import heapq

# Have a dictionary with the coordinates of each of the coordinates, which we 
# Will have to measure and then log in the locations. 

# Initialize the extended graph
graph = {
    'Duncan Hall': [('Crossroad1', 'East', 5), ('Crossroad3', 'South', 7)],
    'Debart Hall': [('Crossroad1', 'West', 5), ('Crossroad2', 'South-East', 6)],
    'Fitzpatrick Hall': [('Crossroad2', 'North-West', 6), ('Crossroad3', 'North', 7)],
    'Crossroad1': [('Duncan Hall', 'West', 5), ('Debart Hall', 'East', 5)],
    'Crossroad2': [('Debart Hall', 'North-West', 6), ('Fitzpatrick Hall', 'South-East', 6)],
    'Crossroad3': [('Duncan Hall', 'North', 7), ('Fitzpatrick Hall', 'South', 7)],
}

# A star's algorithm to find the shortest path
def a_star(graph, start, end):

    open_set = []  
    heapq.heappush(open_set, (0, start))  
    came_from = {}  
    g_score = {node: float('inf') for node in graph}  
    g_score[start] = 0  

    while open_set:
        current_score, current = heapq.heappop(open_set)

        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor, direction, weight in graph[current]:
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))

    return None

# Define a heuristic function (Euclidean distance in this case)
def heuristic(node, goal):
    x1, y1 = get_coordinates(node)
    x2, y2 = get_coordinates(goal)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Helper function to get coordinates from node names
def get_coordinates(node):
    coordinates = {
        'Duncan Hall': (0, 0),
        'Debart Hall': (1, 1),
        'Fitzpatrick Hall': (2, 2),
        'Crossroad1': (1, 0),
        'Crossroad2': (2, 1),
        'Crossroad3': (0, 2),
    }
    return coordinates.get(node)

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

# Take user input for start and end points
start_point = input("Enter the starting point: ")
end_point = input("Enter the end point: ")

# Check if the provided start and end points are valid
if start_point not in graph or end_point not in graph:
    print("Invalid start or end point.")
else:
    # Find and print the shortest path
    shortest_path = a_star(graph, start_point, end_point)
    print(f"Shortest path from {start_point} to {end_point} is: {shortest_path}")
