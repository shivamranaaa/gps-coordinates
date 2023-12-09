import math

def calculate_new_coordinates(current_latitude, current_longitude, distance, direction_degrees):
    # Convert direction to radians
    direction_radians = math.radians(direction_degrees)

    # Calculate Latitude Change
    latitude_change = distance / 111000

    # Calculate Longitude Change
    longitude_change = distance / (111000 * math.cos(math.radians(current_latitude)))

    # Apply Changes to Current Coordinates
    new_latitude = current_latitude + (latitude_change * math.cos(direction_radians))
    new_longitude = current_longitude + (longitude_change * math.sin(direction_radians))

    return new_latitude, new_longitude

# Given current coordinates and parameters
current_latitude = 28.5913768 
current_longitude = 77.3179676
distance = 3853  # in meters
direction_degrees = 233  # in degrees east

# Calculate new coordinates
new_latitude, new_longitude = calculate_new_coordinates(current_latitude, current_longitude, distance, direction_degrees)

# Print the results
print(f"New Latitude: {new_latitude:.6f}")
print(f"New Longitude: {new_longitude:.6f}")
