"""
Write a function called calculate_area that takes base and height as an input 
and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height
"""

def calculate_area(base, height):
    area = (1/2) * base * height
    return area

triangle_base = float(input("Enter the base of the triangle: "))
triangle_height = float(input("Enter the height of the triangle: "))
area_triangle = calculate_area(triangle_base, triangle_height)
print(f"Area of the triangle is {area_triangle:.2f} (unit)^2.")