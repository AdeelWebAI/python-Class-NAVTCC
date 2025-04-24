
# # Open the file in write mode and write to it
# file = open("file.txt", "w")
# show = file.write("hello world \n we are learning python")
# file.close()  # Always close after writing

# # Open the same file in read mode and read the content
# file1 = open("file.txt", "r")
# content = file1.read()
# print("Number of characters written:", show)
# print("File contents:")
# print(content)
# file1.close()


# # Creating a file using 'x' mode (create mode)
# try:
#     with open("myfile.txt", "x") as file:
#         file.write("This file is created using 'x' mode in Python.\n")
#     print("File created successfully.")
# except FileExistsError:
#     print("File already exists.")



# File names to be created




file = open("file.txt", "")


file1 = open("file.txt")
file2 = open("file1.txt")
file3 = open("file2.txt")
file4 = open("file3.txt")
# show = file1.read()
# print(file1.closed)

file = [file1,file2, file3, file4]
file1.close()
file3.close()

for ali in file:
    if ali.closed == False:
        ali.close()
        print(f"the file name: {ali.name} closed sucessfully")
    else:
        print("the file is already closed")
        
        
# show = print(file1.closed)

# for ali in file:
#     ali.close()
#     # print(f"the file name: {ali} closed sucessfully")
