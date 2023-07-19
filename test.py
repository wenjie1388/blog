print("HELLP WORLD")


a = list("Fg asd")
a[0] = a[0].lower()
print("".join(a))

"""
import random

phone = input("")
t = [(random.choice("13579") if int(i) % 2 == 0 else i) for i in list(phone)]
print("".join(t))
"""


def nie():
    for i in range(1, 10):
        for j in range(i, 10):
            print("{:2}*{:2}={:2}   ".format(i, j, i * j), end="")
        print()
