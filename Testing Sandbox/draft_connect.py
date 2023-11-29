from  pathfind import short_path
from  pathfind import get_coordinates
from draft_path_Between_Nodes import two_coordinates_to_distance_and_bearing

start_point = input("Enter the starting point: ")
end_point = input("Enter the end point: ")

node_list = short_path(start_point, end_point)
new_list = []
second_list = []

def from_name_to_coordinates(node_list):
    for node in node_list:
        new_list.append(get_coordinates(node))

    return new_list

def from_coordinates_to_distance(new_list):
    for i in range (0, len(new_list)-1):
        second_list.append(two_coordinates_to_distance_and_bearing(new_list[i], new_list[i+1]))

from_name_to_coordinates(node_list)
from_coordinates_to_distance(new_list)

print(f"Node list: {node_list}")
print(f"New list: {new_list}")
print(f"Second list: {second_list}")

    