class Solution:
    def pairSum(self, head):
        # Fast-slow trick se list ka beech nikaalte hain
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Ab slow second half ke start pe hai, use reverse karte hain
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Head moment se start aur prev se reverse half ke head, dono ko compare karo
        ans = 0
        first = head
        second = prev
        while second:
            # twin sum nikaalo aur max store karo
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans
