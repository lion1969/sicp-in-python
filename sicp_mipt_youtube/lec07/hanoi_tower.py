# 1 + 2 +3 = 6
# i + k + tmp = 6
# tmp = 6 - i - k

def hanoi(n:int, i: int, k: int):
    if n == 1 :
        print("Move disk 1 from pin " + str(i) + " to " + str(k) + ".")
        return
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print("Move disk " + str(n) + " from pin " + str(i) + " to " + str(k) + ".")
        hanoi(n - 1, tmp, k)

hanoi(3, 1, 2)