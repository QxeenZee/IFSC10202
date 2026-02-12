import math

def great_circle_distance(lat1, lon1, lat2, lon2, radius=6371):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    distance = radius * math.acos(
        math.sin(lat1_rad) * math.sin(lat2_rad) +
        math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lon1_rad - lon2_rad)
    )
    return distance

# Get user input for coordinates
print("Enter the latitude and longitude for the first point:")
lat1 = float(input("Latitude 1 (in decimal degrees): "))
lon1 = float(input("Longitude 1 (in decimal degrees): "))

print("Enter the latitude and longitude for the second point:")
lat2 = float(input("Latitude 2 (in decimal degrees): "))
lon2 = float(input("Longitude 2 (in decimal degrees): "))

distance_km = great_circle_distance(lat1, lon1, lat2, lon2)
print(f"The great-circle distance between the two points is {distance_km:.2f} km")