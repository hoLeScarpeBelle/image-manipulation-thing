import random


number = random.randint(0,255)
number = hex(number)
number = number.split('x')
number = number[1]

print("converter number:" + number)