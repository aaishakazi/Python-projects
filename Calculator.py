def add(a,b):
    answer =  a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtract(a,b):
    answer =  a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a,b):
    answer =  a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")    

def divide(a,b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        answer =  a / b
        print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    
    print("Welcome to the calculator!")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit" + "\n")

    choice = input("Enter your choice: ")

    if choice.lower() == "a":
            print("Addition")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            add(a,b)
    elif choice.lower() == "b":
            print("Subtraction")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))    
            subtract(a,b)  
    elif choice.lower() == "c":
            print("Multiplication")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            multiply(a,b)
    elif choice.lower() == "d":
            print("Division")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            divide(a,b)
    elif choice.lower() == "e":
            print("Exiting the calculator. Thnx!")
            quit()
    else:
            print("Invalid input. Please choose from the given options" + "\n")
            