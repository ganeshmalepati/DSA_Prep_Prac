"""
    Docstring for DSA_Day_4

    Why HashMap/Dict is Powerful?
    Operation	Avg Time
    Insert	    O(1)
    Search	    O(1)
    Delete	    O(1)

    Internal Idea (Simple Explanation)

    Key → hash function → index
    Store value at that index
    Python handles collisions internally

                  Set vs Dictionary
    Feature	          Set	        Dictionary
    Stores	          Keys only	    Key-Value
    Duplicates	      ❌	           ❌
    Lookup	          O(1)	        O(1)
    Use case	      Presence	    Count / mapping

    1. Two Sum
    2. First Non-Repeating Character
    3. Subarray with Sum = K
    

"""


"""
    Basic Frequency count in Hashmap/Dictionary 
"""

s = "interview"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


"""
    Two Sum
     
    Example
    nums = [2, 7, 11, 15]
    target = 9
    Output → [0, 1]

    Step-by-step walk-through for [2, 7, 11, 15], target = 9
    Start with seen = {}.
    i = 0, x = 2: complement = 9 - 2 = 7; 7 is not in seen, so store seen[2] = 0 → seen = {2: 0}.
    i = 1, x = 7: complement = 9 - 7 = 2; 2 is in seen with index 0, so return [seen[2], 1] → [0, 1].

    Brute - Force Approach
    ----------------------

    for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

"""



def two_sum_problem(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

arr = [3, 7, 12, 16, 19, 4, 21]
# target = 26
print(two_sum_problem(arr, 26))



def two_sum_all_pairs(nums, target):
    seen = {}
    result = []

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            result.append((seen[diff], i))
        seen[num] = i
    return result

nums = [3, 7, 12, 16, 19, 4, 21]
print(two_sum_all_pairs(nums, 25))



"""
    First Non-Repeating Character

    s = "leetcode"
    Output → 'l'

"""


def first_non_repeat_char_in_string(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s:
        if freq[char] == 1:
            return char
    return None

s = "malayalam"
print(first_non_repeat_char_in_string(s))




def first_non_repeat_char_in_string_using_comprehension(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    return [char for char in s if freq[char] == 1]

s = "malayalam"
print(first_non_repeat_char_in_string_using_comprehension(s))


"""
    Subarray with Sum = K

    nums = [1, 2, 3] -> [1], [2], [3], [1, 2], [2,3]
    k = 3
    Output → 2

    Subarrays: [1,2], [3]

    For nums = [3, 1, 2], k = 3:

    Imp of sum_freq = {0:1}

    At the first element, prefix_sum = 3. You check for 3 - 3 = 0 in the map. 
    If {0: 1} is there, you count the subarray [3] (from index 0 to 0) as valid. Without it, you’d miss this case.

    In summary, {0: 1} is needed to handle cases where a valid subarray starts at the very beginning of the array.
"""


def subarray_brut_force_approach(num, target):
    count = 0
    n = len(num)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += num[j]
            if current_sum == target:
                count += 1
    return count

num = [3, 1, 2, 4, 3]
print(subarray_brut_force_approach(num, 9))


def subarray_sum_optimal_approach(nums, target):
    prefix_sum = 0
    count = 0
    sum_freq = {0:1}
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - target in sum_freq:
            count += sum_freq[prefix_sum - target]
        sum_freq[prefix_sum] = sum_freq.get(num, 0) + 1

    return count, sum_freq

data = [3, 1, 2, 4, 3]
value = [3, 1, 2]
print(subarray_sum_optimal_approach(data, 4))
print(subarray_sum_optimal_approach(value, 4))

from collections import defaultdict

def subarray_sum_optimal_approach_two(nums, target):
    pre_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1
    for i in nums:
        pre_sum += i
        count += freq[pre_sum - target]
        freq[pre_sum] += 1
    return count

nums = [1, -1, 1, -1, 1]
data = [3, 1, 2, 4, 3]
print(subarray_sum_optimal_approach_two(nums, 0))
print(subarray_sum_optimal_approach_two(data, 4))



def subarray_sum_optimal_approach_three(nums, k):
    pref_sum = 0
    idx_map = defaultdict(list)
    idx_map[0].append(-1)
    res = []

    for i, x in enumerate(nums):
        pref_sum += x
        target = pref_sum - k
        if target in idx_map:
            for j in idx_map[target]:
                res.append((j + 1, i))
        idx_map[pref_sum].append(i)

    sub_arrays = [nums[i:j+1] for (i,j) in res]

    return len(res), res, sub_arrays


nums = [1, -1, 1, -1, 1]
print(subarray_sum_optimal_approach_three(nums, 0))




