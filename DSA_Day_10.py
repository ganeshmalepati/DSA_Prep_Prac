"""
    DSA_Day_10
    A Linked List is a linear data structure where:
        Data is stored in nodes
        Each node contains:
            Value (data)
            Pointer/reference to the next node
    📌 Unlike arrays:
        Memory is not contiguous
        Dynamic size
        Insert/Delete is efficient (no shifting)

    SLL:- [Data | Next] -> [Data | Next] -> [Data | None]                 ->> Each node points to the next node only.
    DLL:- None <- [Prev | Data | Next] <-> [Prev | Data | Next] -> None   ->> Each node points to: Next and Previous


    📌 Used in:
        Browser back/forward
        LRU Cache
        Undo/Redo systems

    

"""


class SingleLinkedList:
    def __init__(self, val, Next = None):
        self.val = val
        self.Next = Next



class DoubleLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


"""
    Basic Linked List Operations (Singly)
    1. Insertion Node
        * Insert at Head
        * Insert at Tail
    Traverse until curr.next is None and attach the new node.         --> refer 66 line
    Time is O(n) because you walk the entire list in the worst case.
    
    2. Deletion Node
    3. Traverse


"""

def insert_at_the_head(head, val):
    new_node = SingleLinkedList(val)
    new_node.Next = head
    return new_node



def insert_at_the_tail(head, val):
    new_node = SingleLinkedList(val)
    if not head:
        return new_node
    
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head



def delete_node(head, target):
    if not head:
        return None
    if head.val == target:
        return head.next
    
    prev, curr = head, head.next
    while curr:
        if curr.val == target:
            prev.next = curr.next
            return head
        prev. curr = curr, curr.next
    return head





"""
    Fast & Slow Pointer Technique (VERY IMPORTANT)
    Concept
        Use two pointers:
        Slow → moves 1 step  -->  slow moves one step at a time: slow = slow.next
        Fast → moves 2 steps -->  fast moves two steps: fast = fast.next.next.
    Used to:
        Find middle
        Detect cycle
        Check palindrome
        Find cycle length
    
    If there is a cycle, they eventually meet inside the cycle.
    If there is no cycle and fast reaches None, the list is acyclic.
    For middle element, when fast hits end, slow will be at the middle.
    This pattern gives O(n) time and O(1) extra space without using hash sets

"""


def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next              # store next
        curr.next = prev             # reverse pointer
        prev = curr                  # move prev
        curr = nxt                   # move curr
    return prev




class SLL:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

head = SLL(10)
head.next = SLL(20)
head.next.next = SLL(30)
head.next.next.next = SLL(40)
temp = head

while temp is not None:
    print(temp.data, end=" ")
    # print(temp.next, end=" ")
    temp = temp.next



class SLLTraversal:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(head):
    if head is None:
        print()
        return
    
    print(head.data, end=" ")

    if head.next is not None:
        print("->", end="")
    
    traversal(head.next)

if __name__ == "__main__":
    head = SLLTraversal(10)
    head.next = SLLTraversal(20)
    head.next.next = SLLTraversal(25)
    traversal(head)
