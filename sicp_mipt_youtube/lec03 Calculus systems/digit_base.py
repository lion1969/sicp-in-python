base: int = 7
x = 12
def parse_digit_base(x):
    while x > 0:
        yield x % base
        x //= base

#l = parse_digit_base(x)
lst = []
for dig in (parse_digit_base(x)):
    lst.append(dig)
lst.reverse()
print(lst)