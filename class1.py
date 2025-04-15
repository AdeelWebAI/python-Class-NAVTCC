
# def std1():
#     name = "qadeer"
#     roll_no = 22
#     print(name, roll_no)
# def std2():
#     name = "ali"
#     roll_no = 23
# std1()
# std2()

# class Student:
#     def __init__(self, name , roll_no):
#         self.name = name
#         self.roll_no = roll_no
#     def printProperty(self):
#         print(self.name, self.roll_no)
        

# std1 = Student("ali", 22)
# std1.printProperty()




class student:
    def __init__(self, name , roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def printproperty(self):
        print(self.name)
        print(self.roll_no)
        
obj = student("ali", 22)
obj.printproperty()