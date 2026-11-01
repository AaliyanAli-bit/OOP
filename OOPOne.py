# Project 6: Object-Oriented Programming (OOP) - 1
# Topic: Creating a Class and a Method inside Python

# Step 1: Define the Class (The Blueprint)
class Coder:
    # Constructor method to initialize properties
    def __init__(self, name, grade, language):
        self.name = name
        self.grade = grade
        self.language = language

    # Custom Method inside the class
    def introduce(self):
        print(f"👋 Hello! My name is {self.name}.")
        print(f"🏫 Grade: {self.grade}")
        print(f"💻 Primary Coding Language: {self.language}")

    # Another Method to simulate working on a project
    def build_project(self, project_name):
        print(f"🚀 {self.name} is currently building the '{project_name}' project!")

# Step 2: Main Program Execution

# Create an Object (An instance of the Coder class)
student1 = Coder("Aaliyan", 5, "Python")

# Step 3: Call the methods inside the class
student1.introduce()
print("-" * 40)
student1.build_project("OOP - 1 Assignment")

print("=" * 45)