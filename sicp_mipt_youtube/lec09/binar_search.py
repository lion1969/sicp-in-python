'''
Бинарная сортировка.

(!) Требование: массив должен быть остортирован. По возростанию, для определенности.
Скороксть бинарного поиска O(log_2(N))
'''

def left_bound(A, key):
    left = -1
    right = len(A)
    while right -left > 1 :
        middle = (right + left)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

A = [1, 3, 3, 6, 7, 9]
#    0  1  2  3  4  5
for i in range(-2, 16):
    key = i
    print("Key = ", key, " Left = ", left_bound(A,key), " Right = ", right_bound(A, key))