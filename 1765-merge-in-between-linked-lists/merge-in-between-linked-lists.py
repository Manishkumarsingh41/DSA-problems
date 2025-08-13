# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        # Step 1: 'a' index ke pehle wale node tak jao
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
        
        # Step 2: 'b' index ke baad wale node ko find karo
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
        
        # Step 3: prev_a ke next ko list2 ke head se connect karo
        prev_a.next = list2
        
        # Step 4: list2 ke end tak jao
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        # Step 5: list2 ke end ko after_b se connect karo
        tail2.next = after_b
        
        return list1
