def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1

g = gen_countdown(4)
'''''''''''
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''''''''''
base: int = 7
x = 12
def parse_digit_base(x):
    while x > 0:
        yield x % base
        x //= base

l = parse_digit_base(x)
lst = []
for dig in (l):
    lst.append(dig)
lst.reverse()
print(lst)