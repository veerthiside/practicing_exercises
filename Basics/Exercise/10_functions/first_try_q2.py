"""
Modify above function to take third parameter shape type. 
It can be either "triangle" or "rectangle". 
Based on shape type it will calculate area. 
Equation of rectangle's area is,
rectangle area=length*width
"""

def calculate_area(l1, l2, shape):
    if shape == "triangle":
        area = (1/2) * l1 * l2
    elif shape == "rectangle":
        area = l1 * l2
    return area

shape_name = input(f"Enter the shape 'triangle' or 'rectangle': ").strip().lower()
if shape_name == "triangle" or shape_name == "rectangle":
    length_of_side_one = float(input("Enter the length of side one or height of the triangle: "))
    length_of_side_two = float(input("Enter the length of side two or base of the triangle: "))
    area_of_the_shape = calculate_area(length_of_side_one, length_of_side_two, shape_name)
    print(f"Based on your input the area of the triangle or rectangle is {area_of_the_shape:.2f} (unit)^2.")
else:
    print("Shape not recognisable.")


"""
why stuck?
- the area under else block is statically evaluated as false. - converted [if shape_name == "triangle" or "rectangle"] 
to [if shape_name == "triangle" or shape_name == "rectangle"]. and it worked.
the issue in if shape_name == "triangle" or "rectangle" is that text written in the code, like "rectangle", 
is always True unless it’s an empty string "", so the if statement is true and it executes the code beneath. 
"""