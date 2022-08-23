#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = ((number*-1) % 10)*-1
else:
    last = number % 10

output = f"Last digit of {number} is {last}"

if last > 5:
    output = f"{output} and is greater than 5"
elif last == 0:
    output = f"{output} and is 0"
else:
    output = f"{output} and is less than 6 and not 0"

print(output)
