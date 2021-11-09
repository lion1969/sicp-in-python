# 1 + 2 +3 = 6
# i + k + tmp = 6
# tmp = 6 - i - k

def hanoi(n:int, i: int, k: int):
    if n == 1 :
        print("Move disk 1 from pin", i, "to ", k, ".")
        return
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print("Move disk", n, "from pin", i, "to ", k, ".")
        hanoi(n - 1, tmp, k)

hanoi(4, 1, 2)