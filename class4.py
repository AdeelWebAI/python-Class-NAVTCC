


# class Student:
#     def study(self):
#         print("Let's Study")
        
# class ClassRoom:
#     def __init__(self):
#         self.student_obj = Student()  # Composition: ClassRoom has a Student
        
#     def start_study(self):
#         self.student_obj.study()
#         print("We are going to study")

# exams = ClassRoom()
# exams.start_study()






class student:
    def study(self):
        print("let study")
        
class classRoom:
    def __init__(self):
        self.ali = student()
        print("we are goint to study in the class")
        
obj = classRoom()
obj.ali.study()
obj.ali.student()