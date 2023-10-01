import math
# this function will return the direction and distance that are required to move the car
# in a straight line path from coord_pair_from to coord_pair_to
def two_coordinates_to_distance_and_bearing(coord_pair_from, coord_pair_to):
    
    # Define the coordinates of the two points
    x1, y1 = coord_pair_from[0], coord_pair_from[1]
    x2, y2 = coord_pair_to[0], coord_pair_to[1]

    # Calculate the differences in x and y coordinates
    delta_x = x2 - x1
    delta_y = y2 - y1

    # calculate distance
    distance = ((delta_x) ** 2 + (delta_y) ** 2) ** 0.5

    # Calculate the angle in radians
    angle_radians = math.atan2(delta_y, delta_x)

    # Convert the angle from radians to degrees
    angle_degrees = math.degrees(angle_radians)

    # returning a tuple (distance between nodes, angle between nodes)
    return (distance, angle_degrees)



# this function will essentially do the opposite of two_coordinates_to_distance_and_bearing() in that it will
# return the delta_x and delta_y when given two distance and angle
def distance_and_bearing_to_coordinates(distance, angle_degrees):
    
    # Convert the angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the new coordinates (x2, y2) relative to a starting point (x1, y1)
    x1, y1 = 0.0, 0.0  # Starting point
    x2 = x1 + distance * math.cos(angle_radians)
    y2 = y1 + distance * math.sin(angle_radians)

    delta_x = x2 - x1
    delta_y = y2 - y1

    return (delta_x, delta_y)