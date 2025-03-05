from random import choice as ch
from string import digits as dg

otp = lambda length=6: "".join(ch(dg) for _ in range(length))

for i in range(5):
    # print(otp())
    ...

def otp_func(length=6):
    otp = "".join(ch(dg) for _ in range(length))
    return otp

print(otp_func(17))