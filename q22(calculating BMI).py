print ("\t\t\t***BODY MASS INDEX (BMI) RATIO CALCULATOR***")
print ("Press 1: Metric Conversion \nPress 2: Imperial Conversion")
option = int (input())
if (option == 1):
    w = float (input("Enter weight in kg: "))
    h = float (input("Enter height in meters: "))
    bmi = w / (h**2)
    print ("BMI=",bmi,"kilogram per square meter")
elif (option == 2):
    w = float (input("Enter weight in pounds: "))
    h = float (input("Enter height in inches: "))
    bmi = w / (h**2)
    print ("BMI=",bmi,"pounds per square inch")
else:
    print ("Invalid choice!")
if (bmi < 15):
    print ("Very Severely Underweight!")
elif (bmi >= 15 and bmi < 16):
    print ("Severely Underweight!")
elif (bmi >= 16 and bmi < 18.5):
    print ("Underweight!")
elif (bmi >= 18.5 and bmi < 25):
    print ("Normal (Healthy Weight)!")
elif (bmi >= 25 and bmi < 30):
    print ("Overweight!")
elif (bmi >= 30 and bmi < 35):
    print ("Moderately Obese!")
elif (bmi >= 35 and bmi < 40):
    print ("Severely Obese!")
elif (bmi > 40):
    print ("Very Severely Obese!")