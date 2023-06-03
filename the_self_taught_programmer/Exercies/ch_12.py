import math

# Challenge 1
print('\nChallenge 1:')
class Apple():
    def __init__(self, round, weight, color, sweet):
        self.round = round
        self.weight = weight
        self.color = color
        self.sweet = sweet

apple = Apple(True, 100, 'green', False)
print('My apple is', apple.color)

'''def pr_obj(obj):
    for i in obj:
        print(i)

pr_obj(apple)

TypeError: 'Apple' object is not iterable
'''

# Challenge 2
print('\nChallenge 2:')
class Circle():
    def area(self, crcl_rad):
        self.crcl_rad = crcl_rad
        self.crcl_area = self.crcl_rad ** 2 * math.pi

circle = Circle()
circle.area(6)
print(circle.crcl_area)

# Challenge 3
print('\nChallenge 3:')
class Triangle():
    def area(self, a, b, c):
        s = (a + b + c) * 0.5
        self.triangle_area = (s * (s - a) * (s - b) *( s - c)) ** 0.5

triangle = Triangle()
triangle.area(4, 5, 3)
print(triangle.triangle_area)

# Challenge 4
print('\nChallenge 4:')
class Hexagon():
    def calculate_perimeter(self, a):
        self.perimeter = a * 6

hexagon = Hexagon()
hexagon.calculate_perimeter(6)
print(hexagon.perimeter)