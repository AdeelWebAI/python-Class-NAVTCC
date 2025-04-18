# # class Book:
# #     def __init__(self, pages):
# #         self.pages = pages

# #     def __add__(self, other):
# #         return self.pages + other.pages

# # book1 = Book(100)
# # book2 = Book(150)

# # total_pages = book1 + book2  # uses __add__
# # print("Total pages:", total_pages)  # Output: Total pages: 250


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

# p1 = Person("Alice", 25)
# p2 = Person("Bob", 25)
# p3 = Person("Charlie", 30)

# print(p1 == p2)  # True, same age
# print(p1 == p3)  # False, different age



class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        
    def __add__(self, other):
        return student(self.name + other.name, self.marks + other.marks )
    
s1 = student("ali", 70)
s2 = student("ahmad", 90)

total_marks = s1.marks + s2.marks
names = s1.name + s2.name

print(total_marks, names)