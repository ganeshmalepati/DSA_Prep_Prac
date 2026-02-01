"""
    Docstring for DSA_Day_6
    A sliding window keeps a contiguous range [left, right] over an array/string and moves it instead of recomputing everything for each subarray.
    Maintain:
        Two indices: left (start), right (end)
        Some state: sum, frequency map, count of valid items, etc.

    1️⃣ Fixed Window
        Window size = constant (k)
        Used when:
            “Maximum / minimum sum of subarray of size k”
            “Average of k elements”

    2️⃣ Variable Window
        Window size = dynamic
        Used when:
            “Longest / shortest substring”
            “At most / exactly k
        Constraints based on condition

        left = 0
        window = {}
        n = ""

        for right in range(n):
            # expand window
    
            while "condition_invalid" != True:
                # shrink window
                left += 1
        pass
        
    
    Problems-Solved
    ---------------

    1. Longest Substring Without Repeating Characters
    2. Maximum Sum Subarray (Fixed Window)            -> "Refer Day 4" contains subarray with sum k
    3. Minimum Window Substring

    
"""





"""
    Longest Substring Without Repeating Characters in a string
    Intuition
    Need substring (contiguous) + no repeating chars → variable window on string.
    Use:    
        left, right pointers
        last_index dict: char → last index seen
    When we see s[right] already in current window:
    Move left to max(left, last_index[char] + 1) so we skip the previous occurrence.

    🧠 Sliding Window Insight
        Maintain a window of unique characters
        If duplicate appears → shrink window

    🔹 Step-by-Step Logic
        Use set to track characters
        Expand right pointer
        If duplicate → move left until valid
"""


def longest_substring_without_repeat_char(s):
    last_index = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= left:
            # Move 'left' just past the previous occurrence of 'ch
            left = last_index[ch] + 1
        last_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

s = "abcabcbb"
print(longest_substring_without_repeat_char(s))


def longest_substring_set_use_case(s):
    seen = set()
    left = 0
    max_length = 0
    best_left = best_righ = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            best_left, best_righ = left, right
    return max_length, s[best_left:best_righ+1]

s = "ganeshmalepati"
print(longest_substring_set_use_case(s))



def longest_substring_set_use_case(s):
    seen = set()
    left = 0
    max_length = 0
    best_start = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        cur_len = right - left + 1
        if cur_len > max_length:
            max_length = cur_len
            best_start = left
    return max_length, s[best_start:best_start + max_length]

s = "😀😃😄😁😆😅😄"
new_string = "ganeshmalepati"
print(longest_substring_set_use_case(new_string))
print(longest_substring_set_use_case(s))





"""
    Maximum Sum Subarray (Fixed Window)
    Idea:
        Compute the sum of the first window (arr[0:k]).
        Slide the window by 1 position each step:
            Remove the element leaving the window.
            Add the new element entering the window.
        Track the maximum sum and the best window indices.

    “This is a fixed-size sliding window problem.
    Instead of recalculating the sum for every window, 
    I reuse the previous window’s sum by subtracting the outgoing element and adding the incoming one.
    This reduces time complexity from O(nk) to O(n).”
"""

def max_sum_subarray(my_data, target):
    window_sum = sum(my_data[:target])
    max_sum = window_sum

    for i in range(target, len(my_data)):
        window_sum += my_data[i]
        window_sum -= my_data[i-target]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [3, 5, 12, 8, 2, 3, 7, 4, 9, 11]
x = 4
print(max_sum_subarray(arr, x))




def max_sum_subarray(my_data, target):
    """
    Docstring for max_sum_subarray
    
    :param my_data: [3, 5, 12, 8, 2, 3, 7, 4, 9, 11]
    :param target: 4
    For printing the max subarray elements
    """
    window_sum = sum(my_data[:target])
    max_sum = window_sum
    start = 0

    for i in range(target, len(my_data)):
        window_sum += my_data[i]
        window_sum -= my_data[i-target]
        if window_sum > max_sum:
            max_sum = window_sum
            start = i-target+1
    return max_sum, my_data[start:start+target]

arr = [6, 3, 5, 12, 8, 2, 3, 7, 4, 9, 11]
x = 5
print(max_sum_subarray(arr, x))





"""
    Minimum Window Substring
    Strategy
        Build a frequency map need for t (Counter(t)).
        Expand the window by moving right across s, updating window_count.
        Track formed: how many distinct characters currently meet the required count (window_count[ch] >= need[ch]).
        When formed == required, shrink from the left (left) to minimize the window while keeping it valid.
        Continuously track the best (minimum) window.

    We maintain:
        need → required characters from t
        window → current window counts
        have → how many required characters are satisfied
"""

from collections import Counter

def minimum_substring_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    
    need = Counter()
    window = {}
    have, need_count = 0, len(need)

    res = [-1, -1]
    res_len = float('-inf')
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            # update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # shrink window
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""


s = "ADOBEC"
t = "ABC"
print(minimum_substring_window(s, t))


"""
    Expand → "ADOBEC"
    Contains A, B, C ✔
    Try shrink → fails
    Expand → "CODEBANC"
    Shrink → "BANC" ✔ (smallest)

"""