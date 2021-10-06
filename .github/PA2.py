# Programmer: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 10/5/21
# Programming Assignment: 2
# Program Inputs: Month and Year
# Program Outputs: Display how many days are in that month on that year

# Define Function
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap
# Inputs
month = int(input("Input Month: "))
year = int(input("Input Year: "))
# Check if Month is a Valid Number
if month > 12 or month < 1:
    print("Invalid Month")
# Check if Year is a Leap Year
if is_leap(year) is True and month == 2:
    print("This month has 29 days.")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("This month has 31 days.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("This month has 30 days.")
elif is_leap(year) is False and month == 2:
    print("This month has 28 days.")
