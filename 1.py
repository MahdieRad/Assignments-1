import math

while True:
    print("+")
    print("-")
    print("*")
    print("/")
    print("Sin")
    print("Tan")
    print("Cot")
    print("Pow")
    print("Sqrt")
    print("Factoril")
    print("Radian")


    Oprtr = input(" Opertor: ")
    

    A = int(input("Enter Num: "))
    
    if Oprtr == "+" or Oprtr == "-" or Oprtr == "*" or Oprtr == "/":
        B = int(input("Enter 2 number: "))

    if Oprtr == "+":
        Rslt = A + B

    elif Oprtr == "-":
        Rslt = A - B

    elif Oprtr == "*":
        Rslt = A * B
    elif Oprtr == "/":
        Rslt = A / B
    elif Oprtr == "Sin":
        Rslt = math.sin(A)
    elif Oprtr == "Tan":
        Rslt = math.tan(A)
    elif Oprtr == "Cot":
        Rslt = 1 / (float(math.tan(A)))
    elif Oprtr == "Pow":
        Rslt = A ** B
    elif Oprtr == "Sqrt":
        Rslt = math.sqrt(A)
    elif Oprtr == "Factoril":
        Rslt = math.factorial(A)
    elif Oprtr == "Radian":
        Rslt = A*(180/(math.pi))

    print(Rslt)
