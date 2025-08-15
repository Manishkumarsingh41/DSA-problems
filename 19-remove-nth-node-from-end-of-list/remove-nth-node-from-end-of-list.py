class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Dummy node lagana hai head se pehle -> edge cases handle karna hai
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Fast ko n steps aage bhejna hai -> gap create karna hai
        for _ in range(n):
            fast = fast.next

        # Dono ko saath chalana hai jab tak fast end tak na pahunch jaye
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Slow ke baad wala node remove karna hai
        slow.next = slow.next.next

        # Final head return karna hai
        return dummy.next
