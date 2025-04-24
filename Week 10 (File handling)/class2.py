# ---------- for TXT files---------------#
# with open("file.txt", "w") as file:
#     file.write("this is a file")
    
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)


# reading CSV files


# import csv

# with open("file.csv","r") as file:
#     content = csv.DictReader(file)
#     for row in content:
#         print(row)






# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# import csv
# with open("sample.csv", "r") as file:
#     content = csv.Reader(file)
#     for show in content:
#         print(show)


# import csv

# with open("sample1.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     data = [
#         ["name", "age", "city"],
#         ["Ali", 25, "Lahore"],
#         ["Sara", 30, "Karachi"]
#     ]
#     writer.writerows(data)


    
    # for show in content:
    #     print(show)



# with open("sample.csv", "r") as file:
    
    



import csv
with open("sample1.csv", "w", newline="") as file:
    content = csv.writer(file)
    # content.writerow(["Name", "age", "City"])
    # content.writerow(["adeel", 30, "fsd"])
    listt = [
        ["Name", "age", "City"],
        ["adeel", 30, "fsd"],
        ["ali", 30, "fsd"],
        ["ahmad", 30, "fsd"]
    ]
    content.writerows(listt)