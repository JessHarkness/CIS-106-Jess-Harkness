# This program takes an input age in years
# and converts it to months, days,
# hours, and seconds.
# References:
# https://blog.prepscholar.com/how-many-seconds-in-a-day-a-month-a-year

def get_years():
    print("Enter your age in years:")
    years = int(input())
    return (years)
    
    
def calculate_months(years):
    months_per_year = 12
    months = years * months_per_year
    return (months)


def calculate_days(years):
    days_per_year = 365
    days = years * days_per_year
    return (days)


def calculate_hours(days):
    hours_per_day = 24
    hours = days * hours_per_day
    return (hours)


def calculate_seconds(hours):
    seconds_per_hour = 60 * 60
    seconds = hours * seconds_per_hour
    return (seconds)


def display_result(years, months, days,
                   hours, seconds):
    print(str(years) + " years is: " + str(months) + 
          " months, " + str(days) + 
          " days, " + str(hours) + " hours, " + 
          str(seconds) + " seconds.")

    
def main_function():
    years = get_years()
    months = calculate_months(years)
    days = calculate_days(years)
    hours = calculate_hours(days)
    seconds = calculate_seconds(hours)
    display_result(years, months, days, hours, seconds)


main_function()
