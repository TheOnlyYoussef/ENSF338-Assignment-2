import timeit as t
import matplotlib.pyplot as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
def mod_func(n, memoization={}):
    if n == 0 or n == 1:
        return n
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = mod_func(n-1, memoization) + mod_func(n-2, memoization)
        return memoization[n]
def main():
    x_values = list(range(36))
    yfunc = []
    ymodfunc = []
    for i in x_values:
        time_func = t.timeit(lambda: func(i), number=100)
        yfunc.append(time_func)
        time_modfunc = t.timeit(lambda: mod_func(i), number=100)
        ymodfunc.append(time_modfunc)
    print(f"{time_func:.3f}")
    print(f"{time_modfunc:.10f}")
    plt.plot(x_values, yfunc, label="function")
    plt.plot(x_values, ymodfunc, label="modified function")
    plt.xlabel("n value"); plt.ylabel("Time(s)")
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()
