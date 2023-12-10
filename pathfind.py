# Libraries
import heapq
import math
import sys

# Updated graph with connections between nodes
graph = {
    'Duncan Hall': [('Crossroad1', 'East'), ('Crossroad2', 'North')],
    'Debart Hall': [('Crossroad1', 'East'), ('Crossroad4', 'North'), ('Crossroad5', 'West')],
    'Fitzpatrick Hall': [('Crossroad1','South'),('Crossroad4', 'South')],
    'Riley Hall': [('Crossroad2', 'West'), ('Crossroad3', 'East'), ('Crossroad4','West')],
    'Morris Inn': [('Crossroad5', 'Northeast')],
    'Crossroad1': [('Duncan Hall', 'West'), ('Debart Hall', 'West'), ('Fitzpatrick Hall', 'North')],
    'Crossroad2': [('Duncan Hall', 'South'), ('Riley Hall', 'East')],
    'Crossroad3': [('Riley Hall', 'West'), ('Crossroad4', 'West')],
    'Crossroad4':[('Fitzpatrick Hall', 'North'), ('Debart Hall', 'South'), ('Riley Hall', 'East'), ('Crossroad3', 'East')],
    'Crossroad5':[('Fitzpatrick Hall', 'North'), ('Debart Hall', 'East'), ('Duncan Hall', 'East'), ('Morris Inn', 'West')],
}

# A star algorithm
def a_star(graph, start, end):
    # Priority queue to store nodes with their f_scores
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Dictionary to store the node that came from the current node
    came_from = {}

    # Dictionary to store the actual cost from the start node to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        # Get the node with the lowest f_score from the priority queue
        current_score, current = heapq.heappop(open_set)

        # If the current node is the goal, reconstruct and return the path
        if current == end:
            return reconstruct_path(came_from, current)

        # Explore neighbors of the current node
        for neighbor, direction in graph[current]:

            # Calculate the tentative g_score from the start node to the neighbor
            tentative_g_score = g_score[current] + heuristic(current, neighbor)

            # If the tentative g_score is less than the recorded g_score, update values
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                # Calculate the f_score for the neighbor and add it to the priority queue
                f_score = g_score[neighbor] + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))

    # If the loop completes without finding the goal, return None (no path found)
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

# Dictionary mapping node names to their corresponding coordinates
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

# Reconstruct the path from the 'came_from' dictionary
def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

# Check if the start and end points are valid nodes in the graph
def short_path(start_point, end_point):
    if start_point not in graph or end_point not in graph:
        print("Invalid start or end point.")
        sys.exit()
    else:
        # Find and print the shortest path using A* algorithm
        shortest_path = a_star(graph, start_point, end_point)
        print(f"Shortest path from {start_point} to {end_point} is: {shortest_path}")
    return shortest_path

if __name__ == "__main__":
    # Get user input for start and end points
    start_point = input("Enter the starting point: ")
    end_point = input("Enter the end point: ")

    # Call the 'short_path' function to find and print the shortest path
    short_path(start_point, end_point)