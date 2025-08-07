class Solution:
    def pairSum(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head, prev = head.next, prev.next

        return ans
