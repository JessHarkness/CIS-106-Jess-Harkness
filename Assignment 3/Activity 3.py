# This program converts an input distance in miles to distance in kilometers, meters, and centimeters.
miles = float(26.2)
km = miles * 1.609344
m = km * 1000
cm = m * 100
print("Kilometers:" + str(km))
print("Meters:" + str(m))
print("Centimeters:" + str(cm))
