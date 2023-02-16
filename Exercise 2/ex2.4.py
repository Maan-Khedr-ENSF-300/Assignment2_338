import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):

    half = (start + end) // 2
    if array[half] < array[start]:
        array[start], array[half] = array[half], array[start]
    if array[end] < array[start]:
        array[start], array[end] = array[end], array[start]
    if array[half] < array[end]:
        array[half], array[end] = array[end], array[half]
    
    p = array[half]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while array[i] < p:
            i += 1
        j -= 1
        while array[j] > p:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
