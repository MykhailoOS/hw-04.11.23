import timeit
a = '''def count_fib():

    def fib(n):
        if n == 0 or n == 1:
            return 1
        number = fib(n - 1) + fib(n - 2)
        return number
    return fib

f = count_fib()
print(f(100))'''
print(timeit.timeit(a, number=10))

def func(num1, num2, num3):
    fun_list = [num1, num2, num3]

    def func2():
        get_sum = sum(fun_list)
        return get_sum
    return func2


f = func(1, 2, 3)

result = f()
print(result)


