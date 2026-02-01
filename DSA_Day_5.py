"""
    Docstring for DSA_Day_5
    Two pointers is a technique where you use two indices that move either:

    -> Toward each other (left/right pointers) for problems like reverse, palindrome, container with most water.
        Used in:
            Palindrome
            Container with most water
            Sorted array problems
    -> In the same direction (fast/slow) for problems like removing duplicates from sorted arrays, partitioning.
        Used in:
            Remove duplicates
            Cycle detection
            Linked list problems
    -> Around a center (expand around center) for palindromic substrings (bonus).
        Used in:
            Sliding window
            Subarray problems

    🧠 Pattern recognition cues
    -> Array is sorted → likely two pointers (e.g., remove duplicates, two-sum, 3Sum).
    -> Max/min area/length with endpoints → often left/right pointers (e.g., container with most water).
    -> Characters with symmetry → palindrome checks.
    -> Rearrangement around pivot/value → partitioning (QuickSort, Dutch Flag).

    "“Since the array is sorted, I can eliminate unnecessary comparisons by moving pointers intelligently.”"

    Problems Solved
    1. Reverse of a string
    2. Palindrome Check and Palindrome Case Insensitive Non Alphanumeric      -> "Refer Day 3 4th Problem"
    3. Classic fast-slow pointer problem Remove duplicate elements from a list 
    4. Longest Palindrome Length
    5. Find all unique triplets
    6. Container With Most Water



"""

def reverse_of_string(original_string):
    s = list(original_string)
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

original_string = "Ganesh Malepati"
print(reverse_of_string(original_string))


def Palindrom_check(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = 'radar'
print(Palindrom_check(s))



def palindrome_case_insensitive_non_alphanumeric(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "12 A man, a plan, a canal: Panama 21"
print(palindrome_case_insensitive_non_alphanumeric(s))




"""
    Classic fast-slow pointer problem
    Remove duplicate elements from a list/array using two pointer technique
    -> Array is sorted
    -> Duplicates are adjacent
    -> Use slow pointer to track unique elements
"""

def remove_duplicate_from_list(arr):
    if not arr:
        return 0
    
    i = 0
    result = set()
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
        result.add(i)
    return i+1, result

arr = [0,0,1,1,1,2,2,3,3,4,5,5,6,8]
print(remove_duplicate_from_list(arr))


"""
    Palindrome Patterns (Frequency / Greedy) Longest Palindrome Length 
    Concept: Count characters. Use pairs fully; any odd counts contribute one center character.
    Formula: sum((count // 2) * 2 for all chars) + (1 if any odd exists else 0).
    Why it works: Palindromes have mirror symmetry requiring pairs; one odd-count can be placed in the center.
    Complexity: Time O(n), Space O(k) (distinct chars).
"""

from collections import Counter

def longest_palindrome_length(txt):
    freq = Counter(txt)
    length = 0
    has_odd = False

    for c, cnt in freq.items():
        length += (cnt//2)*2
        if cnt % 2 == 1:
            has_odd = True
    return length + (1 if has_odd else 0)

txt = "ganeshmalepati"
data = "Aa1!1a"
print(longest_palindrome_length(data))
print(longest_palindrome_length(txt))





"""
    Problem: Find all unique triplets (i, j, k) such that 'nums[i] + nums[j] + nums[k] == 0'.
    Concept: Sort the array, fix i, and move left/right inward to match target = -nums[i]. 
    Skip duplicates around i, left, and right.
    Why it works: Sorting enables ordered searching; sum monotonicity guides pointer movement.
    Complexity: Time O(n^2), Space O(1) (excluding output).

"""

def unique_triplet_sum_3sum(nums):
    nums.sort()                         # Step 1: Sort the arra
    res = []                            # To collect triplets
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
             # Skip duplicate 'i' values to avoid repeated triplets
            continue
    left, right = 1, len(nums)-1            # Two-pointer window
    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            res.append([nums[i], nums[left], nums[right]])
             # Skip duplicates for 'left'
            while left < right and nums[left] == nums[left+1]:
                left += 1
            # Skip duplicates for 'right'
            while left < right and nums[right] == nums[right+1]:
                right -= 1
            # Move both pointers inward after recording a valid triplet
            left += 1
            right -= 1
        elif total < 0:
            # Need a larger sum → move 'left' rightward
            left += 1
        else:
            # Need a smaller sum → move 'right' leftward
            right -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(unique_triplet_sum_3sum(nums))



"""
    Container With Most Water
    🧠 Two Pointer Insight
        Width decreases when pointers move
        Area depends on minimum height
        Move the shorter pointer

    🔍 Why Move Shorter Pointer?
        Taller one doesn’t help if width shrinks
        Only possibility to increase area is finding taller bar
    
    Ref Link:- https://www.geeksforgeeks.org/dsa/container-with-most-water/

"""

def container_with_most_water(data):
    left, right = 0, len(data)-1
    max_water = 0
    while left < right:
        water = min(data[left], data[right]) * (right -left)
        max_water = max(max_water, water)

        if data[left] < data[right]:
            left += 1
        else:
            right -= 1
    return max_water

data = [2, 1, 8, 6, 4, 6, 5, 5]
print(container_with_most_water(data))

