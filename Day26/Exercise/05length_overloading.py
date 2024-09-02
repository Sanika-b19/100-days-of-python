# Exercise 5: Overload the " len() " Function

import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2 + self.z**2))

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

vector = Vector(3, 4, 5)
print(f"Vector: {vector}")
print(f"Magnitude of the vector (as integer): {len(vector)}")
