"""
Изначально все числа простые
"""
N = 100
A = [True]*N
A[0] = A[1] = False

for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k)
            A[m] = False

print(A)