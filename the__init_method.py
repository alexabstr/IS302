class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm

    def speak(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old.")


adam = Person("Adam", 47, 193)
lovelace = Person("Lovelace", 24, 178)
lucre = Person("Lucre", 13, 154)

adam.speak()
("Hello! My name is Adam. I am 47 years old.")
lovelace.speak()
("Hello! My name is Lovelace. I am 24 years old.")
lucre.speak()
("Hello! My name is Lucre. I am 13 years old.")
        
        