from random import choices
from string import digits

otp = lambda length=6: "".join(choices(digits, k=length))

for i in range(5):
    # print(otp())
    ...


def otp_func(length=6):
    otp = "".join(choices(digits, k=length))
    return otp


print(otp_func())
