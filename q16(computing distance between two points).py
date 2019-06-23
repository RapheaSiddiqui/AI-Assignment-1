import math
print ("\t\t\t***FINDING DISTANCE BETWEEN TWO GIVEN POINTS***")
x1 = float (input ("Enter x-coordinate of 1st point: "))
y1 = float (input ("Enter y-coordinate of 1st point: "))
x2 = float (input ("Enter x-coordinate of 2nd point: "))
y2 = float (input ("Enter y-coordinate of 2nd point: "))
distance = math.sqrt(((x1-x2)**2) +((y1-y2)**2))
print ("The distance between ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+") is", distance)