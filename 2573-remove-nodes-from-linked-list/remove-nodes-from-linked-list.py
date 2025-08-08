# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNodes(self, head):
        # Step 1: Reverse linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Ab prev reversed list ka head hai

        # Step 2: Traverse reversed list & remove chhote nodes
        max_val = prev.val   # ab tak ka max
        curr = prev
        dummy = curr  # dummy pointer start me
        while curr and curr.next:
            if curr.next.val < max_val:
                # Agar next node ka value chhota hai → skip karo
                curr.next = curr.next.next
            else:
                # Max update karo
                max_val = curr.next.val
                curr = curr.next

        # Step 3: Reverse wapas to get original order
        prev = None
        curr = dummy
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
