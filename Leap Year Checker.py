'''A leap year is a leap year if:
    1. It is divisible by 4
    2. It is not divisble by 100, unless it is also divisible by 400 '''

year = int(input("Enter a year: "))         # takes input from the user and converts it to an integerfor calculation

if year % 4 == 0:               # check if the year is divisible by 4
    if year % 100 == 0:         # check if year is divisible by 100
        if year % 400 == 0:     # check if year is also divisible by 400. Must be divisible by 400 if 100 does it
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")     # year is divisible by 4 but not by 100, not a leap year
else:
    print(f"{year} is not a leap year")     # if first condition is false, it is not a leap year
