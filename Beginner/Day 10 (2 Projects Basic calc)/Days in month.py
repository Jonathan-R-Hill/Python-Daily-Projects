def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap


def days_in_month(leap, month):
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = month - 1
    num_of_days = month_days[month]

    if month == 1:
        if leap == True:
            num_of_days = 29
            print(num_of_days)
            
        else:
            print(num_of_days)
            
    else:
        print(num_of_days)
    
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days_in_month(leap = is_leap(year), month = month)

