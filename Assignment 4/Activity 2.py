# This program will convert a user's age (years) to months, days, hours, seconds.

print("Enter your age in years.")
age = int(input())

months = age * 12
days = age * 365
hours = days * 24
seconds = hours * 3600

print("You are:")
print(months, "months", days, "days", hours, "hours", seconds, "seconds", "old")