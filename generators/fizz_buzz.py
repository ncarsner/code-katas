import math as m


def roundtens(x):
    return int(m.floor(x / 10.0)) * 10


sep = "-"

fval = 5
ftxt = "Fizz"
bval = 7
btxt = "Buzz"
tens = 40
ttxt = "Tens"
oval = 8
otxt = "Eights"
dval = 11
dtxt = "Doubles"

# default range set to end at 2nd occurrence of "FizzBuzz" value
for n in range(1, 101):
    if n % bval == 0 and n % fval == 0:
        print(n, sep, ftxt, btxt)
    elif n % fval == 0:
        print(n, sep, ftxt)
    elif n % bval == 0:
        print(n, sep, btxt)
    elif roundtens(n) == tens:
        print(n, sep, ttxt)
    else:
        # will print only qualified entries
        next
# will print all numbers and results in range
# print(n)
