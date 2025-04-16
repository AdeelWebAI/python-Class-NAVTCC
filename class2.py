


class student:      # defining the name of the class that is a template or blueprint or a design 
    def __init__(self, name , roll_no):    # this is a standard OOP constructor to initialize a class 
        self.name = name    # properties to add in the class and for further use 
        self.roll_no = roll_no
        
    def printproperty(self):  # A method to print the properties defined in it
        print(self.name)    # properties 
        print(self.roll_no)

class person(student):  # another class that is inherited from parent class.
    def __init__(self):
        print("this is our overrided init method")
    
    def printproperty(self):   # method that is overriding the parent class print method.
        print("this is our class of advance python")
        # super().printproperty()      # "Super()" method is used to get the properties of parent class
    
    
# obj = student("ali", 22)   # object that is getting the parent class "student".
# obj.printproperty()

obj1 = person()    # object that using the child class "person".
obj1.printproperty()     # method to print property using the print method 




# multiple inheritance in OOP



class father:
    print("father profession is a teacher")
    
class mother:
    print("mother's occupation is a housewife")
    
class child(father, mother):
    print("child's profession is advance python student")
    
    
ali = child()
print(ali)