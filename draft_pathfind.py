import heapq
import math

# Updated graph with connections between nodes
graph = {
    'Duncan Hall': [('Crossroad1', 'East'), ('Crossroad2', 'North')],
    'Debart Hall': [('Crossroad1', 'East'), ('Crossroad4', 'North'), ('Crossroad5', 'Southwest')],
    'Fitzpatrick Hall': [('Crossroad1','South'),('Crossroad4', 'South')],
    'Riley Hall': [('Crossroad2', 'West'), ('Crossroad3', 'East'), ('Crossroad4','West')],
    'Morris Inn': [('Crossroad5', 'Northeast')],
    'Crossroad1': [('Duncan Hall', 'West'), ('Debart Hall', 'West'), ('Fitzpatrick Hall', 'North')],
    'Crossroad2': [('Duncan Hall', 'South'), ('Riley Hall', 'East')],
    'Crossroad3': [('Riley Hall', 'West'), ('Crossroad4', 'West')],
    'Crossroad4':[('Fitzpatrick Hall', 'North'), ('Debart Hall', 'South'), ('Riley Hall', 'East'), ('Crossroad3', 'East')],
    'Crossroad5':[('Fitzpatrick Hall', 'North'), ('Debart Hall', 'East'), ('Duncan Hall', 'East'), ('Morris Inn', 'West')],

}


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

        for neighbor, direction in graph[current]:
            tentative_g_score = g_score[current] + heuristic(current, neighbor)

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))

    return None

def heuristic(node1, node2):
    # Haversine formula to calculate distance between two lat/lng points
    lat1, lng1 = get_coordinates(node1)
    lat2, lng2 = get_coordinates(node2)
    R = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def get_coordinates(node):
    coordinates = {
        'Duncan Hall': (41.699018, -86.235565),
        'Debart Hall': (41.69889, -86.23652),
        'Fitzpatrick Hall': (41.99530, -86.236295),
        'Riley Hall': (41.699427, -86.235644),
        'Morris Inn': (41.698191, -86.239049),
        'Crossroad1': (41.699016, -86.236491),
        'Crossroad2': (41.69925, -86.235627),
        'Crossroad3': (41.699356, -86.236295),
        'Crossroad4': (41.699348, -86.236527),
        'Crossroad5': (41.698829, -86.237048),
    }
    return coordinates[node]

def short_path(start_point, end_point):
    if start_point not in graph or end_point not in graph:
        print("Invalid start or end point.")
    else:
        shortest_path = a_star(graph, start_point, end_point)
        print(f"Shortest path from {start_point} to {end_point} is: {shortest_path}")
    return shortest_path

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

start_point = input("Enter the starting point: ")
end_point = input("Enter the end point: ")

if start_point not in graph or end_point not in graph:
    print("Invalid start or end point.")
else:
    shortest_path = a_star(graph, start_point, end_point)
    print(f"Shortest path from {start_point} to {end_point} is: {shortest_path}")


