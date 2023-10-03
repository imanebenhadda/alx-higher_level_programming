#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    n = number % 10
    print(f"last digit of {number} is {n} and is greater than 5")
elif number % 10 == 0:
    n = number % 10
    print(f"last digit of {number} is {n} and is 0")
else:
    n = number % 10
    print(f"last digit of {number} is {n} and is less than 6 and not 0")
