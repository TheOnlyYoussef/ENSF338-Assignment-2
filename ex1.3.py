def mod_func(n, memoization={}):
    if n == 0 or n == 1:
        return n
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = mod_func(n-1, memoization) + mod_func(n-2, memoization)
        return memoization[n]