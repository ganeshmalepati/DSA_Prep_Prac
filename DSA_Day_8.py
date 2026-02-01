"""
    DSA_Day_8
    Linear search
        Idea: Scan every element from left to right until you find the target or reach the end

    Check elements one by one
    Works on any array
    No precondition (array need not be sorted)

    “This works, but we can optimize if the array is sorted.” Then we can go for a binary searhc method

    Binary Search:
        Works on sorted arrays
        Repeatedly divides search space into half
        Eliminates half elements each step

    🔸 When to Use Binary Search?
        ✔ Array is sorted
        ✔ Looking for exact element / boundary / minimum / maximum

    ⏱ Time: O(log n)
    📦 Space: O(1)

    
    Problems-Solved
    1. Linear Search Approach
    2. Binary-Search Approach
    3. Lower & Upper Bound Approach
    4. First & Last Position of a Element in a list 
    5. Search in rotated sorted array/list using BS approach
    6. Square root or nearest square root of a given non-negative integer

"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [23, 5, 64, 74, 83, 36, 19, 57]
print(linear_search(arr, 83))



def binary_search_approach(arr, target):
    arr.sort()
    print(arr)
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [23, 5, 64, 74, 83, 36, 19, 57]
print(binary_search_approach(arr, 74))




"""
    Lower Bound & Upper Bound ⭐⭐⭐
    ❓ What Are They?
        Lower Bound → first position where arr[i] >= target
        Upper Bound → first position where arr[i] > target
    
    Used in:
        Range queries
        Frequency counting
        First & last position problems

    📌 Difference is just <= vs < — interviewers LOVE this detail.
"""

def lower_bound_code(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            return left



def upper_bound_code(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
            
    return left


def first_last_position_of_element_list(arr, target):
    left, right = lower_bound_code(arr, target), upper_bound_code(arr, target)-1

    if left <= right and left < len(arr) and arr[left] == target:
        return [left, right]
    right [-1, -1]

arr = [5,5,7,7,8,8,9,10,10]
print(first_last_position_of_element_list(arr, 10))



"""
    Search in Rotated Sorted Array
    🧠 Key Insight
        One half is always sorted
        Identify sorted half
        Decide where to go
    🔹 Step-by-Step Logic
        Find mid
        Check which side is sorted
        Narrow search space
    
"""

def search_in_rotated_sorted_array(num, target):
    left, right = 0, len(num)-1

    while left <= right:
        mid = (left + right) // 2

        if num[mid] == target:
            return mid
        
        if num[left] <= num[mid]:
            if num[left] <= target < num[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        else:
            if num[left] < target <= num[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

num = [4,5,6,7,0,1,2,3]
print(search_in_rotated_sorted_array(num, 3))




"""
    Problem: Given non-negative integer n, compute floor of sqrt(n), i.e. largest integer x such that x*x <= n.

    This is classic binary search on answer:
        Answer x lies in [0, n] (for n >= 1).
        Condition: x*x <= n.
        Monotonic:
        If some x satisfies x*x <= n, then all y <= x also satisfy

    Examples:- 
        x = 0 → 0
        x = 1 → 1
        x = 8 → 2 (since 2²=4 ≤ 8 < 3²=9)
        x = 16 → 4

"""

def sqaure_root_of_integer(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    left, right = 1, n
    ans = 0
    while left <= right:
        mid = (right + left) // 2

        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid -1
    return ans

n = 17
print(sqaure_root_of_integer(n))



