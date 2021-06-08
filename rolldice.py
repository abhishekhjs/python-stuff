import random
import math


# the dice roll question
def roll_dice(sides, times):
    for x in range(times):
        print(random.randint(1, sides))
    print("That's All")


roll_dice(6, 3)
# the subtraction question
print('''
          ''')


def subtractNumbers(x, y):
    return x - y


print(subtractNumbers(3, 1))

print('''
            ''')


# check if a number is odd anf return true or false
def odd(x):
    return x % 2 != 0


print(odd(62))

print('''
          ''')


# returns the fourth power of a number
def fourthPower(x):
    return x ** 4


print(fourthPower(2))

print('''
           ''')


# returns log square sin cosine
def mathwork(x):
    print(math.sin(x))
    print(math.cos(x))
    print(x ** 2)
    print(math.log(x))


mathwork(2)

print('''
           ''')


# fixing error
def intDiv(x, a):
    while x >= a:
        count = 1
        count += 1
        x = x - a
        return count


print(intDiv(5, 3))

print('''
           ''')
# ticktacktoe with and without variables

print("__|____|____|____|__")
print("__|____|____|____|__")
print("__|____|____|____|__")
print("__|____|____|____|__")
print("  |    |    |    |")
