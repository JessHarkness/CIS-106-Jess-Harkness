# This program asks a user to input any month
# of any year, and tells them the number of days
# in that month.
# References: https://www.timeanddate.com/calendar/months/
# References: https://www.mathsisfun.com/leap-years.html
# References: https://realpython.com/python-modulo-operator/

def main():
    month_names_list = ['0', 'January', 
                   'February', 'March', 'April',
                   'May', 'June', 'July', 'August', 'Spetember',
                   'October', 'November', 'December']
    month_days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        year = get_year()
        month_number = get_month_number()
        month_name = get_month_name(month_number, month_names_list)
        month_days = get_month_days(year, month_number, month_days_list)
        if not (year >= 1582) or (month_number in (1, 12)):
            break
        display_days(month_name, month_days, year)
    
    
def get_year():
    print("Enter the year that you are looking for information from:")
    year = int(input())
    
    return year


def get_month_number():
    print("Enter the number of any month (1 = January, 2 = February, etc.):")
    month_number = int(input())
    
    return month_number


def get_month_name(month_number, month_names_list):
    month_name = month_names_list[month_number]
    
    return month_name


def get_month_days(year, month_number, month_days_list):
    month_days = month_days_list[month_number]
    if month_number == 2 and year % 4 == 0 and year % 400 == 0:
        month_days = 29
    
    return month_days


def display_days(month_name, month_days, year):
    print('In ' + str(year) + ', there are ' + 
          str(month_days) + ' days in ' + str(month_name))
    
    
main()
