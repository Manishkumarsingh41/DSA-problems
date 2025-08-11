# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # dummy node banaya start ke liye
        dummy.next = head
        group_num = 1       # group ka size start se 1 hai
        curr = head
        prev = dummy        # prev ko dummy se start karenge

        while curr:
            count = 0
            group_start = curr    # group ka starting node

            # group_num tak nodes traverse karo ya jab tak list khatam na ho
            while curr and count < group_num:
                curr = curr.next
                count += 1
            
            # agar group length even hai toh reverse kar do
            if count % 2 == 0:
                prev.next = self.reverse_group(group_start, count)
                
                # prev ko group ke end pe le jao after reverse
                for _ in range(count):
                    prev = prev.next
            else:
                # agar odd hai toh prev ko group ke end pe simple le jao
                for _ in range(count):
                    prev = prev.next

            group_num += 1    # agle group ke liye size bada do

        return dummy.next


    def reverse_group(self, head, k):
        curr = head
        prev = None

        # simple k nodes ko reverse karne ka logic
        while k > 0:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            k -= 1
        
        # reversed group ka last node ab curr se jodega
        head.next = curr

        # naya head return karo (jo last node tha original mein)
        return prev
