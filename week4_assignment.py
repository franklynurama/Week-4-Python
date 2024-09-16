# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alex", 25, "male")

# Call the introduce method to display the person's information
person1.introduce()
