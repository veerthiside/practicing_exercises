"""
Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and
returns area, circumference and diameter. 
You should get these values in your main program by calling circle_calc function and then print them
"""
import math
def circle_calc(radius):
    area = round(math.pi * pow(radius, 2), 2)
    circumference = round(2 * math.pi * radius, 2) 
    diameter = round(radius * 2, 2)

    return area, circumference, diameter

radius = float(input("Enter the radius of the circle: "))
area, circumference, diameter = circle_calc(radius)
print(f"Area: {area} (unit)^2, Circumference: {circumference} (unit), Diameter: {diameter} (unit)")


""" 
(first_try_q3.py)
why stuck? 
- getting "none" as a second result. - that's bcoz of this line:
return print(f"Area: {area} (unit)^2, circumference:{circumference} (unit), and diameter: {diameter} (unit).").
first python prints, then return gives back a value, but print doesn't give a value so return prints "none".
"""