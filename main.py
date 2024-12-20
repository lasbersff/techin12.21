import json
import math

file_path = 'coordinates.txt' 
with open(file_path, 'r') as file:
    data = json.load(file)
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
def route_distance(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))

route_distances = [route_distance(route) for route in data]
longest_route = max(route_distances)
shortest_route = min(route_distances)
difference = round(longest_route - shortest_route, 2)

print(f"Longest Route: {longest_route:.2f}")
print(f"Shortest Route: {shortest_route:.2f}")
print(f"Difference: {difference:.2f}")
