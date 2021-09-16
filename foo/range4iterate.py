"""
A = [1, 2, 3, 4, 5]
for k in range(5):
    print(k)

B = [0] * 10

print("-=-=-=-=-=-=-=-=-")

for k in range(10):
   print(B[k])
"""

A = [0]*1000
top = 0
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())

for k in range (top - 1, -1, -1):
    print(A[k])
