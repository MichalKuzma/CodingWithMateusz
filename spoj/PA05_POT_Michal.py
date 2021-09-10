def power_last_digit(base, index):
    base = base % 10
    if index == 0:
        return 0
    if base == 1:
        return 1

    last_digits = [
        [0],
        [1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6],
        [5],
        [6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1]
    ]

    return last_digits[base][(index % len(last_digits[base])) - 1]


d = int(input())
for i in range(d):
    a, b = input().split()
    print(power_last_digit(int(a), int(b)))