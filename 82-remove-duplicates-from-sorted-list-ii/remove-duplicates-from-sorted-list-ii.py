# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # dummy node banaya taki head safe rahe
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # last unique node
        curr = head   # current node
        
        while curr:
            # agar agle node ka value same hai
            if curr.next and curr.val == curr.next.val:
                # pura duplicate block skip karo
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # prev ke aage, duplicate ke baad wala node laga do
                prev.next = curr.next
            else:
                # unique hai toh prev ko aage badha do
                prev = curr
            # curr ko har baar aage badhao
            curr = curr.next
        
        # dummy ke baad wala node return karna hai
        return dummy.next