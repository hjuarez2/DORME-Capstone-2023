#Libraries
from  draft_pathfind import short_path
from  draft_pathfind import get_coordinates
from  draft_path_Between_Nodes import two_coordinates_to_distance_and_bearing

# Lists to store Cartesian and Polar coordinates
cartesian_coordinate_list = []
polar_coordinate_list = []

# Convert node names to Cartesian coordinates
def from_name_to_coordinates(node_name_list):
    for node in node_name_list:
        cartesian_coordinate_list.append(get_coordinates(node))

    return cartesian_coordinate_list

# Calculate distances and bearings between consecutive Cartesian coordinates
def from_coordinates_to_distance(cartesian_coordinate_list):
    del polar_coordinate_list[:] # Clear the polar coordinates list
    for i in range (0, len(cartesian_coordinate_list)-1):
        # Calculate distance and bearing between two coordinates
        distance_and_bearing = two_coordinates_to_distance_and_bearing(cartesian_coordinate_list[i], cartesian_coordinate_list[i+1])
        # Modify the distance value (scaling factor) and create a new tuple
        first_value = distance_and_bearing[0]
        modified_tuple = (84922.48010 * first_value, distance_and_bearing[1])
        polar_coordinate_list.append(modified_tuple)
    
    return polar_coordinate_list

if __name__ == "__main__":
    # Get user input for start and end points
    start_point = input("Enter the starting point: ")
    end_point = input("Enter the end point: ")

    # Find the shortest path between start and end points
    node_name_list = short_path(start_point, end_point)

    # Convert node names to Cartesian coordinates to distance and bearings
    cartesian_coordinate_list = from_name_to_coordinates(node_name_list)
    polar_coordinate_list = from_coordinates_to_distance(cartesian_coordinate_list)

    print(f"Second list: {polar_coordinate_list}")

    