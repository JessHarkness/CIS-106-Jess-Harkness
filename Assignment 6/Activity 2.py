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
    months = years * 12
    return (months)


def calculate_days(years):
    days = years * 365
    return (days)


def calculate_hours(days):
    hours = days * 24
    return (hours)


def calculate_seconds(hours):
    minutes_per_hour = hours * 60
    seconds = minutes_per_hour * 60
    return (seconds)


def display_result(years, months, days,
                   hours, seconds):
    print(str(years) + " years is: " + str(months) + 
          " months, " + str(days) + 
          " days, " + str(hours) + " hours, " + 
          str(seconds)+ " seconds.")
def main ():
years = get_years()
months = calculate_months(years)
days = calculate_days(years)
hours = calculate_hours(days)
seconds = calculate_seconds(hours)
display_result(years, months, days, hours, seconds)

main ()
