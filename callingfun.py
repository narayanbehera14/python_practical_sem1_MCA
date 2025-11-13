# Function definition
def calculate_area(length, width):
    area = length * width
    return area

# Example usage with user input
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

result = calculate_area(length, width)
print(f"The area of a rectangle with length {length} and width {width} is: {result}")

# Example usage with fixed values
result = calculate_area(10, 5)
print(f"The area of a rectangle with length 10 and width 5 is: {result}")
