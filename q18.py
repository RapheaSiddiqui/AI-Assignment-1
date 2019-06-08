import math
print ("\t\t\t***CALCULATING HYPOTENUSE OF A RIGHT ANGLE TRIANGLE***")
Base = float (input("Enter length of base: "))
Perp = float (input("Enter length of perpendicular: "))
Hyp = math.sqrt((Base**2)+(Perp**2))
print ("Length of Hypotenuse will be",Hyp)