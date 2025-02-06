# functions in python

def circlearea():
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    print("Area of circle is = %.2f" %area)

def reactanglearea(length, breadth):
    area = length * breadth
    print("Area of the rectangle = %.2f" %area)

def trianglearea(ht, base):
    area = 0.5 * ht *base
    print("Area of rectangle = %.2f" %area)

circlearea()
reactanglearea(5,10)
trianglearea(2, 6)

# using modules

import geometry # type: ignore
geometry.rectanglearea()
print("Calculating area of recatangle")
rlength = float(input("Enter length : "))
rbreadth = float(input("Enter breadth : "))
geometry.rectanglearea(rlength, rbreadth)
print("Calculating area of triangle")
rheigth = float(input("Enter heigth : "))
rbase = float(input("Enter base : "))
geometry.trianglearea(rheigth, rbase)