def noar_sort(A):
    if len(A) < 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    noar_sort(L)
    noar_sort(R)

AA = [0,1,2,3,4,5]
LL = ['a', 'b']
MM = ['c', 'd']
RR = ['e','f']
AA =