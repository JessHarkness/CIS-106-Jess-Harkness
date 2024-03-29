# This program asks a user to input any month
# of any year, and tells them the number of days
# in that month.
# References: https://www.timeanddate.com/calendar/months/
# References: https://www.mathsisfun.com/leap-years.html
# References: https://realpython.com/python-modulo-operator/

def main():
    month_names_list = ['January', 
                   'February', 'March', 'April',
                   'May', 'June', 'July', 'August', 'Spetember',
                   'October', 'November', 'December']
    month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        year = get_year()
        month_number = get_month_number()
        if ((year < 1582) or (month_number > len(month_names_list)) or
                (month_number <= 0)):
            break
        month_name = get_month_name(month_number, month_names_list)
        month_days = get_month_days(year, month_number, month_days_list)
        display_days(month_name, month_days, year)
    
    
def get_year():
    print("Enter a year:")
    year = int(input())
    
    return year


def get_month_number():
    print("Enter the number of any month (1 = January, 2 = February, etc.):")
    month_number = int(input())
    
    return month_number


def get_month_name(month_number, month_names_list):
    month_name = month_names_list[month_number - 1]
    
    return month_name


def get_month_days(year, month_number, month_days_list):
    month_days = month_days_list[month_number - 1]
    if (month_number == 2 and year % 4 == 0 and 
            year % 100 != 0 or year % 400 == 0):
        month_days = 29
    
    return month_days


def display_days(month_name, month_days, year):
    print(str(month_name) + ' ' + str(year) + 
          ' has ' + str(month_days) + ' days.')
    
    
main()
