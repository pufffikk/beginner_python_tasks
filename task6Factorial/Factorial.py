import sys
sys.set_int_max_str_digits(100000)


def factorial(num: int):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)


def factorial_loop(n):
    stack = list(range(2, n + 1))
    result = 1
    while stack:
        result *= stack.pop()
    return result


print(factorial_loop(10000))
try:
    print(factorial(1000))
except RecursionError:
    print("maximum recursion depth exceeded")
