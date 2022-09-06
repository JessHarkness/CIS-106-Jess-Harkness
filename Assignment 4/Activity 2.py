# This program will take a user's age in years and convert it to months, days, hours, and seconds.

print("Enter your age in years.")
age = int(input())

months = age * 12
days = age * 365
hours = days * 24
seconds = hours * 3600

print("You are:", months, "months", "," ,days, "days", "," ,hours, "hours", "," ,seconds, "seconds", "old")
