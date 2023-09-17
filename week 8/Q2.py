class Circle:
    _pi = 3.141  # Private member variable for pi

    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def display_list(self):
        print("List:", self.numbers_list)

    def calculate_area(self, radius):
        return Circle._pi * radius * radius

# Example usage:
numbers_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(numbers_list)
circle_instance.display_list()

radius = 5
area = circle_instance.calculate_area(radius)
print(f"Area of a circle with radius {radius} is {area}")