#determine if a specified year is a leap year


def isLeapYear(year):
   if(current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0)):
      return True

   else:
       return False




if(__name__=="__main__"):
   x = True
   while x:
      current_year = int(input("enter a year: "))

      if(isLeapYear(current_year)):
         print(current_year, " is a leap year")

      else:
          print(current_year, " is NOT a leap year")

      y = input("\ntype \"quit\" to stop \nor \npress enter to continue... ")
      if y == "quit":
         x = False
      print()
      #os.system("pause")

