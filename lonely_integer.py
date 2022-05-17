a1 = [1,2,3,4,1,2,3]
a2 = [1,2,4,4,1,2,3]
a3 = [1,2,5,9,1,2,5]

all_a = [a1, a2, a3]

def lonely_integer(a):
    for i in a:
        if a.count(i) == 1:
            return i

for i in all_a:
    print(lonely_integer(i))