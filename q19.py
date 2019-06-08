print ("\t\t\t***DISTANCE CONVERSION CALCULATOR***")
print ("Press 1: ft--->inch \nPress 2: ft--->yard \nPress 3: ft--->mile")
option = int (input())
if (option == 1):
    length_ft1 = float (input("Enter length in ft: "))
    inches = 12*length_ft1
    print (length_ft1,"is equal to",inches,"inch")
elif (option == 2):
     length_ft2 = float (input("Enter length in ft: "))
     yards = (1/3)*length_ft2
     print (length_ft2,"is equal to",yards,"yard")
elif (option == 3):
     length_ft3 = float (input("Enter length in ft: "))
     miles = (1/5280)*length_ft3
     print (length_ft3,"is equal to",miles,"mile")
else:
    print ("Invalid choice!")