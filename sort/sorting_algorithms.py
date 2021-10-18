import random

def selection_sort(t):
    i = 0
    for i in range(len(t) - 1):
        min_index = i
        j = i + 1
        for j in range(len(t)):
            if t[min_index] > t[j]:
                min_index = j
                j += 1
        t[i] , t[min_index] = t[min_index] , t[i]
        i += 1

    
    return t

def bubble_sort(t):
    i = 0
    for i in range(len(t) - 1):
        j = 0
        for j in range(len(t) - 1):
            if t[j] > t[j + 1]:
                t[j] , t[j + 1] = t[j +1] , t[j]
            j += 1
        i += 1
    
    
    return t

def merge_sort(t):


    return t

x = random.sample(range(0, 100), 10)
print('Input List:\t', x)

print('Selection Sort:\t', selection_sort(x))
print('Bubble Sort:\t', bubble_sort(x))
print('Merge Sort:\t', merge_sort(x))