t = (12, 20, 33, 45)

student ={
    "name":"ali",
    "age": 22,
    "marks":80
}
var = 0
for key,value in student.items():
    if key == "marks":
        print(f"key found: name{var}")
        break
    else:
        var += 1
        print(key,value)