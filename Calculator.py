import sys, time
x = 0
y = 0

def add():
    print("Give the first number")
    x = int(input())
    print("Give the second number")
    y = int(input())
    z = x + y
    print("Addition of", x, " and ", y, "equals =", z)
    time.sleep(1)

def sub():
    print("Give the first number")
    x = int(input())
    print("Give the second number")
    y = int(input())
    z = x - y
    print("Subtraction of", x, " and ", y, "equals =", z)
    time.sleep(1)

def mul():
    print("Give the first number")
    x = int(input())
    print("Give the second number")
    y = int(input())
    z = x * y
    print("Multiplication of", x, " and ", y, "equals =", z)
    time.sleep(1)

def div():
    print("Give the first number")
    x = int(input())
    print("Give the second number")
    y = int(input())
    z = x / y
    print("Division of", x, " and ", y, "equals =", z)
    time.sleep(1)

while True:
    print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
    5. Exit''')
    choice = input()
    if choice == '1':
        add()
    elif choice == '2':
        sub()
    elif choice == '3':
        mul()
    elif choice == '4':
        div()
    elif choice == '5':
        sys.exit()
    else:
        print("Give a number between 1 and 5")