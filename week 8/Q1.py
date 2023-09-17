class Circle:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def display_list(self):
        print("List:", self.numbers_list)


numbers_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(numbers_list)
circle_instance.display_list()