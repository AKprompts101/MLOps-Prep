#initiate a class
class employee:    
    #special method - constructor
    def __init__(self):
        print("____________Started exicuting attribute/data____________")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("____________attribute/data have been initiated____________")

    def travel(self,destination):
        print("____________this travel function called manually____________")
        print(f"Employee is not travaling to {destination}")


#creating an object/instance of class
sam = employee()

#printing the attributes
# print(sam.salary)
# print(sam.id)

#calling method
# sam.travel("pune")

print(type(sam))