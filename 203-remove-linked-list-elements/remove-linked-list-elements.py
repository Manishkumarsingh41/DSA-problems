class Solution:
    def removeElements(self, head, val):
        # Dummy ek naya node banaya jo head ke aage rahega
        dummy = ListNode(0)
        dummy.next = head
        
        # Current pointer dummy se start hoga
        current = dummy
        
        # Jab tak list khatam na ho jaaye
        while current.next:
            # Agar next node ka value delete karna hai
            if current.next.val == val:
                # Bypass that node (link tod do)
                current.next = current.next.next
            else:
                # Nahi toh aage badho
                current = current.next
        
        # Dummy ke next se actual head start hota hai
        return dummy.next
