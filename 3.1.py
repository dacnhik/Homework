Num_1 = int(input("Enter first number"))
Num_2 = int(input("Enter second number"))
Oper = str(input("Enter operation"))

if Oper == "+":
    print(Num_1 + Num_2)
elif Oper == "-":
    print(Num_1 - Num_2)
elif Oper == "*":
    print(Num_1 * Num_2)
elif Oper == "/":
    if Num_2 == 0:
        print("cannot be divided by 0")
    else:
        print(Num_1 / Num_2)
else:
    print("Check your data")