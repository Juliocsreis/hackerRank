ex = [3,1,0]

def flippingBits(n):
    return ~n & 0xFFFFFFFF

for i in ex:
    print(flippingBits(i))


print(~'hello')