b = 9

def function(a):
    global b
    print(f"{a} and {b}")
    b = str(10)

function(6)
print(b)

# UnboundLocalError without global b declared inside function