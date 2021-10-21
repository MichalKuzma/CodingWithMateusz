import random

def merge(l, r):
    result = []

    i = 0
    j = 0
    while i < len(l) or j < len(r):
        if j >= len(r) or (i < len(l) and l[i] < r[j]):
            result += [l[i]]
            i += 1
        else:
            result += [r[j]]
            j += 1

    return result

def merge_sort(t):
    if len(t) == 1 or len(t) == 0:
        return t
    
    midpoint = int(len(t) / 2)
    return merge(merge_sort(t[:midpoint]), merge_sort(t[midpoint:]))

x = random.sample(range(0, 100), 10)
print('Input List:\t', x)

print('Merge Sort:\t', merge_sort(x))