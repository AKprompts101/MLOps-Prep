# # Simple Inheritance

# # # base class / parent class

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")



# # # Derived Class/ child class

# class Dog(Animal):
  
#     def speak(self):
#         print(f"{self.name} barks.")



# # # Create an instance of animal
# # animal = Animal("Generic animal")
# # animal.speak() # Output:generic animal makes a sound


# # # Creat an instance of Dog
# dog = Dog("Buddy")
# dog.speak() # Output= buddy barks.

##=================================================================================
# Super Keyword
##=================================================================================
# # Base Class
class Animal:
    def __init__(self):
        self.name = 'Buddy'

    def speak(self):
        print(f"{self.name} makes a sound.")


# # Derived Class
class Dog(Animal):
    def __init__(self, Breed):
        super().__init__()
        self.Breed = Breed

    def speak(self):
        super().speak()    # call the base class method
        print(f"{self.name} barks. It is a {self.Breed}")

# # create an instance of a dog
dog =Dog("Golden retriever")
dog.speak()   
        

