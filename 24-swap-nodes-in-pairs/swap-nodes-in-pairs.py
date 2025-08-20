class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)     # Sabse pahale  dummy node banaya hai 
        dummy.next = head
        prev, curr = dummy, head

        while curr and curr.next:       # jab tak 2 nodes bache hain
            first, second = curr, curr.next

            # swap links
            first.next = second.next
            second.next = first
            prev.next = second

            # move pointers
            prev, curr = first, first.next

        return dummy.next   # new head
