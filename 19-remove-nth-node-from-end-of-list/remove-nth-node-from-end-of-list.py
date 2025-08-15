class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # Fast ko n+1 steps aage bhejna hai -> direct delete point mil jayega
        for _ in range(n+1):
            fast = fast.next
        
        # Jab tak fast None nahi hota, dono ko saath chalana hai
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Node skip karna hai
        slow.next = slow.next.next
        return dummy.next
