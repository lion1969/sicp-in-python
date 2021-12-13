def noar_sort(A):
    if len(A) < 1:
        return
    barrier = A[0]
    L, R, M = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    noar_sort(L)
    noar_sort(R)
    # A = [item for lst in (L, M, R) for item in lst]
    i = 0
    for lst in (L, M, R):
        for element in lst:
            A[i] = element
            i += 1


A = [1, 7, 2, 4, 5, 4, 1, 3, 6, 2, 1]
noar_sort(A)
print(A)
