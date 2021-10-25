import random

def selection_sort(t):
    t = list(t)

    for i in range(len(t)):
        min_index = i
        for j in range(i , len(t)):
            if t[min_index] > t[j]:
                min_index = j
        tmp = t[i]
        t[i] = t[min_index]
        t[min_index] = tmp

    
    return t

def bubble_sort(t):
    t = list(t)

    for i in range(len(t) - 1):
        for j in range(len(t) - 1):
            if t[j] > t[j + 1]:
                tmp = t[j]
                t[j] = t[j + 1]
                t[j + 1] = tmp
        
       
    return t

def merge_sort(t): #nie intuicyjne, dziwne, bąbelkownanie lepszze nie działa, nawet internet nie pomaga, i need help!!!!!!!!!!!!!! 
    t = list(t)

    if len(t) > 1:
        mid = len(t) // 2
        L = t[:mid]
        R = t[mid:]

        sorted_L = merge_sort(L) # nie miałem pojęcia o istnieniu tego zwrotu 
        sorted_R = merge_sort(R)

        merge(t, sorted_L, sorted_R)
        
    return t

def merge(t, L, R):
    i = 0 # left 
    j = 0 # right 
    k = 0 # merged 
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            t[k] = L[i]
            i += 1
        else:
            t[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        t[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        t[k] = R[j]
        j += 1
        k += 1

x = random.sample(range(0, 100), 10)
print('Input List:\t', x)

print('Selection Sort:\t', selection_sort(x))
print('Bubble Sort:\t', bubble_sort(x))
print('Merge Sort:\t', merge_sort(x))