# References: https://www.youtube.com/watch?v=FWaN3lTyhPU I used this video to help me create functions in Flowgorithm.
# This program converts an input distance in miles to distance in kilometers, meters, and centimeters.
print("Please enter a distance in miles.")
miles = float(input())
km = miles * 1.609344
metrs = km * 1000
cm = metrs * 100
print("Kilometers:" + str(km))
print("Meters:" + str(metrs))
print("Centimeters:" + str(cm))
