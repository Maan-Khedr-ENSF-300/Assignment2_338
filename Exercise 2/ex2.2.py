import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def main(): 
    with open("ex2.json","r") as data: 
        text = json.load(data)

    t1 = []
    t2 = []
    count = []

    for i in range(len(text)):
        t1.append(timeit.timeit(lambda: func1(text[i], i , len(text[i])-1), number = 1))
        t2.append(timeit.timeit(lambda: func2(text[i], i , len(text[i])-1), number = 1))
        count.append(i)

    plt.plot(count, t1)
    plt.xlabel("Frequency of func1 being called")
    plt.ylabel("Time")
    plt.show()

    plt.plot(count, t2)
    plt.xlabel("Frequency of func2 being called")
    plt.ylabel("Time")
    plt.show()

if __name__ == "__main__":
    main()

