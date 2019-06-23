print ("\t\t\t***CHECING DIVISIBILITY OF TW0 GIVEN NUMBERS***")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
check = num1%num2
if(check == 0):
    print("Numbers are completely divisible!")
else:
    print("Numbers are not completely divisible!. The remainder is ", check)