
class student:
    def developer(self):
        print("is a developer")
        
class ali(student):
    def developer(self):
        print("is a java developer")
        
class ahmad(student):
    def developer(self):
        print("is a python developer")
        
def dev(student):
    student.developer()
    
dev(ali())
dev(ahmad())
dev(student())





# class ali:
#     def developer(self):
#         print("ali is a developer")
        
# class ahmad:
#     def developer(self):
#         print("ahmad is a developer")

# class qadeer:
#     def developer(self):
#         print("qadeer is a developer")
        
# a = ali()
# b = ahmad()
# c = qadeer()

# print(a.developer())