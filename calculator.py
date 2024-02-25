n1 = n2 = ""

while type(n1) not in (int, float):
  try:
    n1 = eval(input("Enter first number: "))
  except (NameError, SyntaxError):
    print("Enter a valid number\n")

while type(n2) not in (int, float):
  try:
    n2 = eval(input("Enter second number: "))
  except (NameError, SyntaxError):
    print("Enter a valid number\n")

operation = input("Choose Operation (+, -, *, /): ")

if operation == '+':
  print(f"{n1} + {n2} = {n1 + n2}")
elif operation == '-':
  print(f"{n1} - {n2} = {n1 - n2}")
elif operation == '*':
  print(f"{n1} * {n2} = {n1 * n2}")
elif operation == '/':
  if n2 != 0:
    if n1 % n2 == 0:
      print(f"{n1} / {n2} = {int(n1 / n2)}")
    else:
      print(f"{n1} / {n2} = {n1 / n2}")
  else:
    print(f"{n1} / {n2} = Division by zero not possible")
else:
  print("Invalid opration")