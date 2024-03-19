# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:19:24 2024

@author: round
"""
#needed for using pi
import math


class Shape():
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
    
    def area(self):
        return math.pi * (self.side ** 2)
        
    def perimeter(self):
        return math.pi * 2 * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        return self.side * self.width

    def perimeter(self):
        return 2 * (self.side + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(side1)
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side + self.side2 + self.side3) / 2
        return (s * (s - self.side) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side + self.side2 + self.side3
    
#defines the shapes
circle_shape = Circle(4)
rectangle_shape = Rectangle(4, 5)
triangle_shape = Triangle(3, 4, 5)

#Prints the Area/Perimeter
print("Circle Area:", circle_shape.area())
print("Circle Perimeter:", circle_shape.perimeter())

print("Rectangle Area:", rectangle_shape.area())
print("Rectangle Perimeter:", rectangle_shape.perimeter())

print("Triangle Area:", triangle_shape.area())
print("Triangle Perimeter:", triangle_shape.perimeter())
