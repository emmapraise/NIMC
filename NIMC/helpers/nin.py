import random


def generateNin(digits):
    """Method that generate NIN"""

    lower = 10 ** (digits - 1)
    upper = 10**digits - 1
    return random.randint(lower, upper)
