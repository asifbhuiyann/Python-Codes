year=int(input("Enter the year:\n"))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
           print("Program Terminated")
       else:
           print("{0} is not a leap year".format(year))
           print("Program Terminated")
   else:
       print("{0} is a leap year".format(year))
       print("Program Terminated")
else:
   print("{0} is not a leap year".format(year))
   print("Program Terminated")