class Circle:
    _pi = 3.141  # Private class variable for pi

    @classmethod
    def area(cls, radius):
        return cls._pi * radius**2

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls._pi * radius

# Example usage:
radius = 5

area = Circle.area(radius)
perimeter = Circle.perimeter(radius)

print(f"Radius: {radius}")
print(f"Area of a circle with radius {radius} is {area:.2f}")
print(f"Perimeter of a circle with radius {radius} is {perimeter:.2f}")









