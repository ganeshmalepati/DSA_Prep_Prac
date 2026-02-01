"""
    Descreption for DSA_Day_2
    1. Second Largest Element refer Day 1

    2. Move Zeroes to End
      ❓ Problem
      arr = [0, 1, 0, 3, 12]
      Output → [1, 3, 12, 0, 0]

    3. Kadane’s Algorithm ⭐⭐⭐
       ❓ Problem

       Find maximum sum of a contiguous subarray

       arr = [-2,1,-3,4,-1,2,1,-5,4]
       Output = 6  # [4,-1,2,1]

    4. Longest Common Prefix

     ✅ Sliding Window (Good)
     window_sum += arr[right]
     window_sum -= arr[left]
"""


def move_zero_to_end(data):
    pos_zero = 0
    for i in range(len(data)):
        if data[i] != 0:
            data[pos_zero], data[i] = data[i], data[pos_zero]
            pos_zero += 1
    return data

data = [2, 0, 4, 5, 0, 0, 8, 0, 24, 0, 9, 0, 10]
print(move_zero_to_end(data))




"""
    Kadane’s Algorithm Intuition
    At each element, ask:
    Is it better to start a new subarray here or
    extend the existing subarray?
    Find maximum sum of a contiguous subarray

    arr = [-2,1,-3,4,-1,2,1,-5,4]
    Output = 6  # [4,-1,2,1]

    Dry Run (Important for Interviews)
    i	arr[i]	curr_sum	max_sum
    0	-2	        -2	       -2
    1	 1	 max(1, -2+1)=1	    1
    2	-3	 max(-3, 1-3)=-2	1
    3	 4	 max(4, -2+4)=4	    4
    4	-1	 max(-1, 4-1)=3	    4
    5	 2	 max(2, 3+2)=5	    5
    6	 1	 max(1, 5+1)=6	    6
    7	-5	 max(-5, 6-5)=1	    6
    8	 4	 max(4, 1+4)=5	    6
"""

def max_subarray_sum(arr):
    curr_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))




def max_subbarray(arr):
    Max_sum = cur_sum = float('-inf')
    cur_len = 0
    best_left = best_right = 0
    for i, x in enumerate(arr):
        if cur_sum + x < x:
            cur_sum = x
            cur_len = i
        else:
            cur_sum += x
        if cur_sum > Max_sum:
            Max_sum = cur_sum
            best_left, best_right = cur_len, i
    return Max_sum, arr[best_left:best_right+1], (best_left, best_right)


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))




def max_sum_with_subarray_indices(arr):
    curr_sum = max_so_far = float('-inf')
    curr_len = 0
    best_l = best_r = 0
    for i, x in enumerate(arr):
        if curr_sum + x < x:
            curr_sum = x
            curr_len = i
        else:
            curr_sum += x
        if curr_sum > max_so_far:
            max_so_far = curr_sum
            best_l, best_r = curr_len, i
        
    return max_so_far, arr[best_l:best_r+1], (best_l, best_r)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_with_subarray_indices(arr))



"""
    Longest Common Prefix 
"""

def longest_common_prefix(my_list):
    if not my_list:
        return ""
    
    my_list.sort()
    first, last = my_list[0], my_list[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

my_list = ["interview","internet","internal"]
print(longest_common_prefix(my_list))

