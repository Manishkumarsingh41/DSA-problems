class Solution:
    def rotateRight(self, head, k):
        # edge cases — kuch karna hi nahi
        if not head or not head.next or k == 0:
            return head
        
        # length nikal rahe + tail dhoond rahe
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # circular bana rahe
        tail.next = head

        # extra rotation kaat rahe
        k = k % length

        # naya tail dhoondhna hai
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        # naya head set kar rahe
        new_head = new_tail.next

        # circle tod rahe
        new_tail.next = None

        # answer return
        return new_head
