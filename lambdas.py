from random import choice as ch
from string import digits as dg

otp = lambda length=6: "".join(ch(dg) for _ in range(length))

for i in range(5):
    print(otp())