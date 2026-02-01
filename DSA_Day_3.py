"""
    Description for DSA_Day_3 
    -> Efficient String Modification

    -> Why Frequency Map?

       Counting characters
       Anagrams
       Duplicate detection

    -> Two Pointer Technique

    Practice Problems
    1. Reverse of a string using Two pointer technique
    2. Valid Anagram
    3. Palindrome Check 
    4. Case-insensitive & alphanumeric (Interview twist) 
"""


"""
    String Modification
"""

s = "hello"
chars = list(s)
chars[0] = 'H'
s = ''.join(chars)


"""
    Frequency Map
"""
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1



"""
    Two Pointer Technique
"""
left, right = 0, len(s) - 1




def reverse_words(s):
    words = s.split()
    # words = list(s)
    left, right = 0, len(words)-1
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        
    return ''.join(words)

words = "hello world python"
print(reverse_words(words))



"""
    Anagram Check 
"""
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    
    return True

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))


"""
    Palindrome Check 
"""

def is_palindrome(s):
    left, right = 0, len(s)-1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

s = "madam"
print(is_palindrome(s))


"""
   Case-insensitive & alphanumeric (Interview twist) 
"""

def case_insensitive_and_alnum_palindrome_check(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s = "12 A man, a plan, a canal: Panama 21"
print(case_insensitive_and_alnum_palindrome_check(s))


