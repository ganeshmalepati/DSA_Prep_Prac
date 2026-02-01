"""
    DSA_Day_9

    Rearranging elements in a sequence according to a rule (ascending / descending / custom).

    🔹 Comparison vs Non-Comparison Sort
        Type	            Example	                           Time
        Comparison	        Merge, Quick, Bubble	        ≥ O(n log n)
        Non-Comparison	    Counting, Radix	                O(n) (with constraints)
    
    Why is stability important?
        ✔ When sorting by multiple keys (e.g., salary then age).

    Input:  [(2, 'b'), (1, 'a'), (2, 'c')]
    Stable sort → [(1, 'a'), (2, 'b'), (2, 'c')]  # 'b' before 'c'
    Unstable → [(1, 'a'), (2, 'c'), (2, 'b')]    # order may change

    Python's sorted() and list.sort() are stable.



    Comparison sorting
        Definition: Sorting algorithms that compare elements pairwise using <, >, == operators.
        Limitation: Cannot sort faster than O(nlogn) in the average/worst case (information theory bound).

    
    Problems-Solved
    1. Merge_sort_approach
    2. Quick Sort (Partition Based)
    3. Sort_colors (Dutch National Flag)
    4. Merge Intervals (Two Approaches)
    5. Minimum_meeting_rooms_problem 
    6. Minimum Platforms (Railway Version)

"""

"""
    2️⃣ Merge Sort (Divide & Conquer)
    🧠 Idea
        Divide array into halves
        Sort each half
        Merge sorted halves
    
    Time & Space
        Time: O(n log n) (best/avg/worst)
        Space: O(n)
        Stable: ✅

"""

def merge_sort_approach(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_approach(arr[:mid])          # start to mid element in an array/list/dict
    right = merge_sort_approach(arr[mid:])         # mid to end element in an array/list/dict 
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and  j < len(right): # Check the condition
        if left[i] <= right[j]:
            result.append(left[i])           # Add left half element into the result at first
            i += 1
        else:
            result.append(right[j])          # And then Add the right element into the result at last
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [(3, 'a'), (3, 'b'), (1, 'c')]

nums = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort_approach(nums))
print(merge_sort_approach(arr))




"""
   Quick Sort (Partition Based)

   Idea: Pick pivot, partition array (elements < pivot → left, > pivot → right), recurse.​

    🧠 Idea
        Choose pivot
        Move smaller left, larger right
        Recursively sort partitions 
    
    Case	        Time
    Best / Avg	    O(n log n)
    Worst	        O(n²)

    Refer Here:- https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/

"""



def quick_sort_approach_1(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_approach_1(arr, low, pi-1)
        quick_sort_approach_1(arr, pi+1, high)

def quick_sort_approach_2(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_approach_2(arr, low, pi-1)
        quick_sort_approach_2(arr, pi+1, high)
    return arr                                  # <-- return the array


def partition(arr, low, high):
    pivot = arr[high]                           # Lomuto partition
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

arr = [64, 34, 25, 12, 22, 11, 90]
num = [2, 0, 2, 1, 1, 0]
quick_sort_approach_1(arr)                       # sorts in-place
print(arr)

print(quick_sort_approach_2(num))





"""
    arr.sort()          # In-place
    sorted_arr = sorted(arr)  # New list

    Problem:- Sort Colors (Dutch National Flag)

    🧠 Key Idea (3 Pointers)        
        low → next 0 position
        mid → current
        high → next 2 position

"""

def sort_colors(nums):
    """
        Sort 0s, 1s, 2s in-place using Dutch National Flag algorithm.
        Cond_1:- Swap with low pointer (put 0s at beginning)        refer:- if nums[mid] == 0:
        Cond_2:- 1s can stay in middle                              refer:- nums[mid] == 1:
        Cond_3:- Swap with high pointer (put 2s at end)             refer:- else cond
        nums is now sorted: all 0s, then 1s, then 2s
    """
    low, mid, high = 0, 0, len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

nums = [2, 0, 2, 1, 1, 0]
# sort_colors(nums)
# print(nums)

print(sort_colors(nums))





"""
    Problem:- Merge Intervals
    🧠 Steps
        Sort by start
        Merge overlapping intervals

"""

def merge_intervals_problem_approach_one(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    merged = []

    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return [tuple(x) for x in merged]

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals_problem_approach_one(intervals))




def merge_intervals_problem_approach_two(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return [tuple(x) for x in merged]

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals_problem_approach_two(intervals))






"""
    Goal: Find the minimum number of rooms (or platforms) needed so that no two overlapping intervals share a room.
    Approach A (Two-pointer over starts/ends):
     Sort starts and ends separately.
     Sweep:
        If start[i] < end[j] → need a new room (rooms++).
        Else → one meeting finished (rooms--).
        Track max_rooms.
"""

def minimum_meeting_rooms_problem(intervals):
    if not intervals:
        return 0
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)
    rooms = max_rooms = i = j = 0
    while i < len(start):
        if start[i] < end[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j -= 1
    return max_rooms

intervals = [[0,30],[5,10],[15,20]]
print(minimum_meeting_rooms_problem(intervals))

"""
    DRY RUN
    -------
    intervals = [[0,30],[5,10],[15,20]]

    starts = [0,5,15]
    ends   = [10,20,30]

    i=0,j=0 → 0 < 10 → rooms=1
    i=1,j=0 → 5 < 10 → rooms=2
    i=2,j=0 → 15 >= 10 → rooms=1
    i=2,j=1 → 15 < 20 → rooms=2

    ✅ Answer = 2

"""




def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    i = j = 0
    platforms = max_platforms = 0

    while i < len(arrival):
        if arrival[i] <= departure[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

arrival   = [900, 940, 950, 1100, 1500, 1800]
departure = [910,1200,1120,1130,1900,2000]

print(min_platforms(arrival, departure))










""" 
    Key Differences at a Glance of sort() and sorted()

    Feature                     list.sort()                     sorted()
    Type                        List method                     Built-in function
    Works on                    Only lists                      Any iterable (list, tuple, set, dict, generator, etc.)
    Return value                Returns None (sorts in-place)   Returns a new list
    Mutates input               Yes                             No
    Stability                   Stable                          Stable
    Complexity                  O(n log n) (Timsort)            O(n log n) (Timsort)
    MemoryIn-place;             no extra list allocation        Allocates a new list
    
"""