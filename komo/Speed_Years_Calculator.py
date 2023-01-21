import math
a = 0x0000000000000000000000000000000000000000000000020000000000000000
b = 0x000000000000000000000000000000000000000000000003ffffffffffffffff

t = b-a
print("TotalKeys in 65 Bit range:",t)

speed_in_seconds = 1000000000
print("keys per second",speed_in_seconds)
speed_in_minutes = speed_in_seconds*60
print("keys per minutes",speed_in_minutes)
speed_in_hour = speed_in_minutes*60
print("Keys per hour:",speed_in_hour)
speed_in_day = speed_in_hour*24
print("Keys per day:",speed_in_day)
totalrangehours=t/speed_in_day
print("Total Hours to scan full range:",math.floor(totalrangehours))
years=totalrangehours/365
print("Total Years to scan full range:",math.floor(years))
