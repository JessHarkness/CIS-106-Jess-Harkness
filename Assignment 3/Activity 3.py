# This program converts an input distance in miles to distance in kilometers, meters, and centimeters.
miles = float(input())
km = miles * 1.609344
meters = km * 1000
cm = meters * 100
print("Kilometers:" + str(km))
print("Meters:" + str(meters))
print("Centimeters:" + str(cm))
