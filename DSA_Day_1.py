"""
    Docstring for DSA_1
    1. Max Element in an array/list
    2. Reverse a array/list
    3. Rotate Array by K
    4. Second Largest Element
"""

def max_elem(array):
    max_ele = array[0]
    for i in array:
        if i > max_ele:
            max_ele = i
    return max_ele

array = [23, 35, 546, 7457, 2342, 3, 34535, 4564, 8567, 34, 453453, 747, 858, 958]
print(max_elem(array))


def max_array(array):
    return max(array)

array = [23, 35, 546, 7457, 2342, 3, 34535, 4564, 8567, 34, 453453, 747, 858, 958]
print(max_elem(array))


"""
    Reverse a array/list 
"""

def reverse_array(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [34535, 4564, 8567, 34, 453453, 747, 858, 958]
print(reverse_array(arr))


def reverse_list(arr):
    return arr[::-1]

arr = [34535, 4564, 8567, 34, 453453, 747, 858, 958]
print(reverse_array(arr))



"""
    Rotate Array by K
    1. Right Rotation
    2. Left Rotation
"""

def rotate_list_by_k(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

my_list = [1, 2, 3, 4, 5]
x = 2
print(rotate_list_by_k(my_list, x))


def rotate_list_by_k(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

my_list = [1, 2, 3, 4, 5]
x = 1
print(rotate_list_by_k(my_list, x))



def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    
def lef_rotate(arr, k):
    n = len(arr)
    k %= n
    
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr

my_list = [2, 3, 6, 7, 8, 3, 9, 10]
x = 3
print(lef_rotate(my_list, x))
    


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    
def right_rotate(arr, k):
    n = len(arr)
    k %= n
    
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr

my_list = [2, 3, 6, 7, 8, 3, 9, 10]  
# Flow --> [10, 9, 3, 8, 7, 6, 3, 2] -> [3, 9, 10, 8, 7, 6, 3, 2] -> [3, 9, 10, 2, 3, 6, 7, 8]
x = 3
print(right_rotate(my_list, x))



"""
    Second largest Element in an array/list
"""

def second_largest(data):
    first = second = float('-inf')
    for i in data:
        if i > first:
            first, second = i, first
        elif first > i > second:
            second = i
    return second

data = [23422, 5252342, 6235242, 634536, 6345235, 6, 7547, 474, 33463464, 843536]
print(second_largest(data))

