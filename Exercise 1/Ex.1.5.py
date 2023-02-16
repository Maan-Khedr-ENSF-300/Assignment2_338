import timeit
import matplotlib.pyplot as plt
import numpy as np


#timing for the original code
def func_1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func_1(n-1) + func_1(n-2)


elapsed_time_1 = [timeit.timeit(lambda : func_1(i), number = 1) for i in range(0, 35)]

print(f'Elapsed time: {elapsed_time_1} seconds')



#timing for the optimized code
def func_2(n, dict={}):
    if n == 0 or n == 1:
        return n
    if n in dict:
        return dict[n]
    else:
        result = func_2(n-1, dict) + func_2(n-2, dict)
        dict[n] = result
        return result

elapsed_time_2 = [timeit.timeit(lambda : func_2(j), number = 1) for j in range(0, 35)]
print(f'Elapsed time: {elapsed_time_2} seconds')

time_list = [elapsed_time_1, elapsed_time_2]
zero_list = [0, 1]

list_35 = list(range(35))


plt.title("Unoptimized (no memoization)")
plt.plot(list(range(35)), elapsed_time_1)
plt.xlabel("Numbers")
plt.ylabel("Time taken")
plt.show()
plt.title("Memoization / Optimized")
plt.plot(list(range(35)), elapsed_time_2)
plt.xlabel("Numbers")
plt.ylabel("Time taken")
plt.show()



