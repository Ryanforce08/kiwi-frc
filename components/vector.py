import math


class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def rotate(self, angle: float):
        """Rotates the vector by the specified angle (in degrees) and returns a new rotated vector."""
        radians = math.radians(angle)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x_new = self.x * cos_angle - self.y * sin_angle
        y_new = self.x * sin_angle + self.y * cos_angle
        return Vector2d(x_new, y_new)

    def scalarProject(self, other):
        """Projects this vector onto another vector and returns the scalar projection."""
        return (self.x * other.x + self.y * other.y) / math.sqrt(
            other.x**2 + other.y**2
        )
