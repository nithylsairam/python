def leap(year):
    if year % 4 ==0:
        return True
    if year % 100 ==0:
        return False
    if year % 400 ==0:
        return True
    return False

year = int(input("Year:"))
if(leap(year) == True):
    print("It is a leap year")
else:
    print("It is not a leap year")

