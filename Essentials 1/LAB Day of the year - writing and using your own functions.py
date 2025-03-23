#Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.
#Use the previously written and tested functions. Add your own test cases to the code.

def is_year_leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else: return False

def days_in_month(year, month):
    if month==11 or month==4 or month==6 or month==9:
        return 30
    elif month==2:
        if is_year_leap==True: return 29
        else: return 28
    else: return 31

def day_of_year(year, month, day):
    if year<1582 or month<1 or month>12 or day<1:
        return None
    tot_days=0
    for m in range(month-1):
        tot_days+=days_in_month(year, m)
    return tot_days+day
print(day_of_year(2000, 12, 31))