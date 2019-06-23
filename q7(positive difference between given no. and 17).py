print ("\t\t\t***FINDING DIFFERENCE OF A NUMBER AND 17***")
num = float(input("Enter any number: "))
if num < 17 and num >= 0:
    difference = 17 - num
elif num < 0:
    difference = (17 - num) + 1
else:
    difference = num - 17
print("The difference between 17 and", num ,"is", difference)