import calendar

year = int(input("Enter year: "))
month = int(input("Enter Month: "))

# https://docs.python.org/3/library/calendar.html
print(calendar.month(year,month))