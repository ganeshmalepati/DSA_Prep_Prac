"""
    DSA_Day_7

    A recursive function is a function that calls itself on a smaller/simpler version of the same problem, 
    until it hits a base case.

    General pattern for designing recursion:
        Define the problem for “this call” clearly.
        Decide simplest input(s) → base case(s).
        Decide how to move towards base case each call.
        Ensure each call strictly reduces problem size.

    Recursion:- A function that calls itself to solve a smaller version of the same
    "def func():
     func()"
    ❌ This will crash (no stopping condition)

    Two Mandatory Components of Recursion
    1️⃣ Base Case (MOST IMPORTANT)
        Condition where recursion stops
        Prevents infinite calls
    "if n == 0:
     return"

     2️⃣ Recursive Case
        Function calls itself with reduced input
    
    return n * factorial(n - 1)

    📌 If either is missing → stack overflow

    How Recursive Calls Work (STACK CALLS)
        ❓ What is Call Stack?
        Stack stores function calls
        Last call executes first (LIFO)

    factorial(3)
    → 3 * factorial(2)
    → 2 * factorial(1)
    → 1 * factorial(0)
    → return 1

    Stack Unwinding

    factorial(0) → 1
    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6

    
    Problems-Solved
    1. Factorial of number
    2. Fibanocci series
    3. Reverse of string
    4. Reverse of a list/array
    5. Problem Power
"""


def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_number(n-1)

n = 10
print(factorial_number(n))



def factorial_iterative_approach(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5 
print(factorial_iterative_approach(n))



def fibonacci_series_recursive_optimization(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_series_recursive_optimization(n-1, memo) + fibonacci_series_recursive_optimization(n-2, memo)
    return memo[n]

n = 8
print(fibonacci_series_recursive_optimization(n))



def reverse_of_string(s):
    if len(s) == 0:
        return s
    return reverse_of_string(s[1:]) + s[0]

s = "Ganesh"
print(reverse_of_string(s))



def reverse_string_two_pointer_recursive(s, left, right):
    chars = list(s)
    if left >= right:
        return s
    chars[left], chars[right] = chars[right], chars[left]
    return ''.join(reverse_string_two_pointer_recursive(chars, left + 1, right - 1))

s = "ganesh malepati"
print(reverse_string_two_pointer_recursive(s, 0, len(s)-1))



def reverse_of_list(n, left, right):
    """
        You just need to return the list at the base case (and after recursion), 
        or print the list after calling the function.
    """
    if left >= right:
        return n             # return the list when pointers cross
    
    n[left], n[right] = n[right], n[left]
    return reverse_of_list(n, left + 1, right - 1)

arr = [23, 53, 2, 6, 875, 43, 96, 46]
print(reverse_of_list(arr, 0, len(arr)-1))



def reverse_of_list(n, left, right):
    """
        If you prefer not to return the list and just mutate:
    """
    if left >= right:
        return                      # in-place, nothing to return
    
    n[left], n[right] = n[right], n[left]
    reverse_of_list(n, left + 1, right - 1)

arr = [23, 53, 2, 6, 875, 43, 96, 46]
reverse_of_list(arr, 0, len(arr)-1)
print(arr)





"""
    Problem Power(x, n)

    def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)    


    🧠 Insight
        xⁿ = (x²)ⁿ/²
"""


def recursive_power_problem(x, n):
    if x == 0:
        return 1
    
    half = pow(x, n//2)
    if n % 2 == 0:
        return half * half
    else:
        return n * half * half
    
x = 4
print(recursive_power_problem(x, 3))