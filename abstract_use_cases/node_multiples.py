nums = [*(range(50_001))]

for n in nums:
    connections = (n ** 2 - n) // 2
    powers = 10 ** (len(str(n)) - 1)
    r = connections / powers
    if n == r:
        spacer = len(str(nums[-1])) + 2
        print(f"{n:<{spacer},} {connections:>{spacer*2},}")
