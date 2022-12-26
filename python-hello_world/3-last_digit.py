#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last =number % 10
if last == 0:
    line =("last digit of" +str(number) + "is" +str(last) + " and is 0")
else:
    if last >5:
        line =("last digit of" +str(number) + "is" +str(last) + " and is grater"+"than 5")
    elif last <5:
        line =("last digit of" +str(number) + "is" +str(last) + " and is grater"+"than 5")
print(line)
