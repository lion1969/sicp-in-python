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

generate_number(3, 4)
# gen_bin(3)
