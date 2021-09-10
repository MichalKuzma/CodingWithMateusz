def power(basis, index):
    if basis == 0:
        return 0
    if basis == 1:
        return 1
    if index == 0:
        return 1

    last_digits = [
        [0],
        [1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6,],
        [5],
        [6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1]
    ]
    potential_results = last_digits[basis % 10]
    # print(potential_results)
    result = potential_results[(index % len(potential_results)) - 1]

    return result



d = int(input())
for i in range(d):
    a, b = input().split()
    print(power(int(a), int(b)))