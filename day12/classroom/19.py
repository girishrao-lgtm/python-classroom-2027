'''
Example 19 — Operator Overloading
'''
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector(
            self.x * scalar,
            self.y * scalar
        )

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 * 3)
print(3 * v1)
