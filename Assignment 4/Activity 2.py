# This program converts a user's age (years) to months, days, hours, seconds.
# Reference: https://blog.prepscholar.com/how-many-seconds-in-a-day-a-month-a-year

print("Enter your age in years.")
age = int(input())

months = age * 12
days = age * 365
hours = days * 24
seconds = hours * 60 * 60

print("Your age is:")
print(months, "months", days, "days", hours, "hours", seconds, "seconds")
