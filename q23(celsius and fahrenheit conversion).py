print ("\t\t\t***TEMPERATURE CONVERSION***")
print ("Press 1: Celsius--->Fahrenheit \nPress2: Fahrenheit--->Celsius")
option = int (input())
if (option == 1):
    temp1 = float (input("Enter temperature in Celsius: "))
    F = ( temp1 * (9/5) ) + 32
    print (temp1,"Celsius is equal to",F,"Fahrenheit")
elif (option == 2):
    temp2 = float (input("Enter temperature in Fahrenheit: "))
    F = ( temp2 - 32 ) * (5/9)
    print (temp2,"Fahrenheit is equal to",F,"Celsius")
else:
    print ("Invalid Choice!") 