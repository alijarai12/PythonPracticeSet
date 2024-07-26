import pickle_eg, pickle
f = open("student.dat", "wb")
n = int(input("Enter number of student: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    obj = pickle_eg.Student(name, roll)
    pickle.dump(obj, f)

print("objects stored successfully")