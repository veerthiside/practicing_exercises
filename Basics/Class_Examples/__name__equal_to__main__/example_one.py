def square_area (side):
    print("__name__:", __name__)
    area = pow(side, 2)
    return area

if __name__ == "__main__":
    area = square_area(4)
    print(f"Area: {area} (unit)^2") 
    