class Solution:
    def reverseEvenLengthGroups(self, head):
        # helper function: linked list ko reverse karne ke liye
        def reverse(start):
            prev = None
            curr = start
            # simple linked list reverse logic
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # pehle poore list ki length nikal lete hain
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        size = 1  # group ka size start hota hai 1 se
        curr = head
        while curr and length > 0:
            # group ka actual size length ya size me se chhota wala le lo
            group_len = min(size, length)
            length -= group_len  # ab length kam ho gayi group_len se
            
            # tail find karo group ke last node ke liye
            tail = curr
            for _ in range(group_len - 1):
                tail = tail.next
            
            # next group start kaha hoga, uska pointer nikal lo
            nxt_group = tail.next
            tail.next = None  # current group ko tod do
            
            # agar group length even hai toh reverse kar do
            if group_len % 2 == 0:
                prev.next = reverse(curr)   # prev ke next ko reverse wale head se jodo
                curr.next = nxt_group       # ab curr (jo ab tail ban gaya) ko next group se jod do
                prev = curr                 # prev pointer update kar do
                
            else:
                # agar odd group hai toh waise hi chod do, bas link update karo
                prev.next = curr
                prev = tail
                
            # curr ko next group start pe le jao
            curr = nxt_group
            
            # agla group size ek bada kar do
            size += 1
        
        return dummy.next
