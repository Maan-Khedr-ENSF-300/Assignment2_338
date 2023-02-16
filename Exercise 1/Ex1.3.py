def func(n, dict={}):
    if n == 0 or n == 1:
        return n
    if n in dict:
        return dict[n]
    else:
        result = func(n-1, dict) + func(n-2, dict)
        dict[n] = result
        return result


