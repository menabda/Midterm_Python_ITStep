while True:
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    operation = input("Choose Operation: +, -, *, /\n")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if operation == "+":
        print(n1 + n2)
        break
    elif operation == "-":
        print(n1 - n2)
        break
    elif operation == "*":
        print(n1 * n2)
        break
    elif operation == "/":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Division by zero not possible")
        break
    else:
        print("Invalid Operation")