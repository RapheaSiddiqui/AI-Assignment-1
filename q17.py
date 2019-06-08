print ("\t\t\t***CONVERTING FEET/INCHES TO CENTIMETERS***")
print ("Press 1 for ft--->cm")
print ("Press 2 for inch--->cm")
option = int (input())
if (option == 1):
    length_ft = float (input("Enter length in ft: "))
    cm1 = 30.48*length_ft
    print (length_ft,"is equal to",cm1,"cm")
elif (option == 2):
     length_in = float (input("Enter length in inch: "))
     cm2 = 2.54*length_in
     print (length_in,"is equal to",cm2,"cm")
else:
    print ("Invalid choice!")