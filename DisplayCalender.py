import calendar
yy = int(input("Enter year(ex. 2020): "))
mm = int(input("enter month in digit (ex. may = 5: "))
cal = calendar.month(yy, mm)
print(cal)
