a = 10

def change():
    global a
    a = 5
    print("inside function:", a)

change()

print("outside function:", a)
