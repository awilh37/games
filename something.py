# something simple and text based
# runnable through the pi
# NO (crazy) MODULES
from random import randint as random
x=int(input("Give me a number: "))
if input("Give me a word - ") == "random":
    number=random(1,x)
    print(number)
else:
    print("Your word wasn't what I was going for...")