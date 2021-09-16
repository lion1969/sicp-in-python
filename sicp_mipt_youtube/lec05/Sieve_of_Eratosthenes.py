"""
Изначально все числа простые
"""
N = 1000000
N += 1
A = [True] * N
line_step = 100

# print(A)
# exit(0)

A[0] = A[1] = False

for k in range(2, N):
    if A[k]:
        for m in range(2 * k, N, k):
            A[m] = False

Prime_digits_list = [x for x in range(len(A)) if A[x]]
# print(Prime_digits_list)
B = []
tmpAry = []
i = 0
for x in Prime_digits_list:
    cur = x // line_step
    if i == cur:
        tmpAry.append(x)
    else:
        i = i + 1
        if len(tmpAry) > 0:
            B.append(tmpAry)
        tmpAry = []
        if i == cur:
            tmpAry.append(x)

if len(tmpAry) > 0:
    B.append(tmpAry)

Boo = []
for x in B:
    Boo.append(len(x))
Boo.sort()
Bb = {x: None for x in Boo}
Boo = [k  for k,v in Bb.items() ]

print(Boo)
