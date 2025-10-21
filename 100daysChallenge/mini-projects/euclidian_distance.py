import math

p1 = (1, 2, 3)
p2 = (4, 5, 6)
distance = math.dist(p1, p2)
# distance_second = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
# distance_third = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

print(f"First solution (math.dist): {distance:.3f}")
# print(f"Second solution (math.sqrt): {distance_second:.3f}")
# print(f"Third solution (without math module): {distance_third:.3f}")
