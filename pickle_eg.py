# pickling and unpickling example

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.age = roll

    def display(self):
        print(f"name is: {self.name} and roll is: {self.age}")
