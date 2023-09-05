import math


class Shape:
    counter = 0

    def __init__(self):
        Shape.counter += 1
        self.id = Shape.counter

    def print(self):
        print(self.__class__.__name__, "perimeter: ", self.perimeter(), ", area: ", self.area())

    def perimeter(self):
        return None

    def area(self):
        return None

    def __str__(self):
        return "shape"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.id == other.id
        return False


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return (2 * math.pi) * self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def __str__(self):
        return "circle {}".format(int(self.radius))

    def __hash__(self):
        return hash((self.id, self.radius))

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.id == other.id and self.radius == other.radius
        return False


class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.semi_major = max(a, b)
        self.semi_minor = min(a, b)

    def area(self):
        return math.pi * self.semi_major * self.semi_minor

    def eccentricity(self):
        linear_eccentricity = math.pow(self.semi_major, 2) - math.pow(self.semi_minor, 2)
        if linear_eccentricity < 0:
            return None
        return math.sqrt(linear_eccentricity)

    def __str__(self):
        return "ellipse {} {}".format(int(self.semi_major), int(self.semi_minor))

    def print(self):
        print(self.__class__.__name__, "perimeter: ", self.perimeter(), ", area: ", self.area(), ", linear",
                                                                        " eccentricity", self.eccentricity())

    def __hash__(self):
        return hash((self.id, self.semi_major, self.semi_minor))

    def __eq__(self, other):
        if isinstance(other, Ellipse):
            return (
                    self.id == other.id
                    and self.semi_major == other.semi_major
                    and self.semi_minor == other.semi_minor
            )
        return False


class Rhombus(Shape):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def perimeter(self):
        return 2 * math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def area(self):
        return self.x * self.y

    def side(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)) / 2

    def inradius(self):
        if self.x == 0 and self.y == 0:
            return None
        return (self.x * self.y) / (2 * math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

    def __str__(self):
        return "rhombus {} {}".format(int(self.x), int(self.y))

    def print(self):
        print(self.__class__.__name__, "perimeter: ", self.perimeter(), ", area: ", self.area(),
              "side: ", self.side(), " in-radius: ", self.inradius())

    def __hash__(self):
        return hash((self.id, self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Rhombus):
            return self.id == other.id and self.x == other.x and self.y == other.y
        return False
