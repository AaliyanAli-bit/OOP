# Project 7: Object-Oriented Programming (OOP) - 2
# Topic: Circle Area & Perimeter using Class Methods

import math

# Step 1: Define the Circle Class
class Circle:
    # Constructor to set radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate perimeter (circumference)
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Step 2: Main Program

# Get radius input from user
user_radius = float(input("Enter the radius of the circle: "))

# Create an object instance of Circle
shape = Circle(user_radius)

# Step 3: Display results using class methods
print("\n--- CALCULATED RESULTS ---")
print(f"Radius Entered: {shape.radius}")
print(f"🔵 Area of Circle: {shape.calculate_area():.2f}")
print(f"⭕ Perimeter (Circumference): {shape.calculate_perimeter():.2f}")
print("=" * 50)