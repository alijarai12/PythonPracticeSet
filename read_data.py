import pickle

f1 = open("student.dat", 'rb')

while True:
    try:
        data = pickle.load(f1)
        data.display()
    except EOFError:
        print("End of file reached")
        break

f1.close()