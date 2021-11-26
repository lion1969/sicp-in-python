def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    gen_bin(M - 1, prefix + "0")
    gen_bin(M - 1, prefix + "1")

def generate_number(N: int, M: int, prefix=None):
    """
    Генерирует все числа (с лидирующими нулями)
    N-ричной системе счисление (N<=10) длины М.
    :param N: Система Счисления
    :param M: длина числа
    :param prefix: префикс
    :return:
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()
def find(number, A):
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(N: int, M=-1, prefix=None):
    """
    Генерация перестановок N чисел в M позициях, с префиксом prefix.
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(6,6)
#generate_number(3, 4)
# gen_bin(3)
