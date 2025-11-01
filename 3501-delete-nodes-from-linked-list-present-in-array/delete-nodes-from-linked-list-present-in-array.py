class Solution(object):
    def modifiedList(self, nums, head):
        remove = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val in remove:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
