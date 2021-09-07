import math


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def sito(upper_bound):
    result = [True] * (upper_bound + 1)
    result[0] = False
    result[1] = False

    for i in range(2, int(math.sqrt(upper_bound)) + 1):
        if result[i]:
            for j in range(i * 2, upper_bound + 1, i):
                result[j] = False

    return result


n = int(input())

s = sito(10000)

for i in range(n):
    # if is_prime(int(input())):
    if s[int(input())]:
        print('TAK')
    else:
        print('NIE')
