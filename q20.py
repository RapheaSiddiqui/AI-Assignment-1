print ("\t\t\t***TIME IN SECONDS***")
hrs = float (input("Enter hours: "))
mins = float (input("Enter minutes: "))
sec1 = hrs * 3600
sec2 = mins * 60
sec = sec1 + sec2
print (hrs,"hours =",sec1,"seconds")
print (mins,"minutes =",sec2,"seconds")
print ("Total =",sec,"seconds!")