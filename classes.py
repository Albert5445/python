class Rectengle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"This is a Rectengle with weight {self.width} , height {self.height}"


    def __repr__(self):
        return "This is a Rectengle code "

    def __eq__(self, other):
        if isinstance(other , Rectengle):
           return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectengle):
            return self.area() < other.area()
        else:
            return NotImplemented
    def __le__(self, other):
        if isinstance(other, Rectengle):
            return self.area() <= other.area()
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Rectengle):
            return self.area() > other.area()
        else:
            return NotImplemented
    def __ge__(self, other):
        if isinstance(other , Rectengle):
            return self.area() >= other.area()
        else:
            return NotImplemented


r1 = Rectengle(10, 20)
r2 = Rectengle(100, 200)

print(r1 < r2)
