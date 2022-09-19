class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hascycle(head, pos):
    if not head:
        return False
    
    slow = head
    fast = head.next
    while slow and fast and fast.next:
        if slow==fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

head = [3,2,0,-4]
pos = 1
print("Linked List Cycle", hascycle(head, pos))