class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        # Step 1: Dummy node banaya jo sorted list ko point karega
        dummy = ListNode(0)

        # Step 2: Current node jo unsorted list me traverse karega
        curr = head

        # Jab tak unsorted nodes bache ho
        while curr:
            # Step 3: Pata karna hai next node ko abhi, kyunki curr ka pointer todne wale hain
            next_temp = curr.next

            # Step 4: dummy se search karenge sahi jagah insert karne ke liye
            prev = dummy

            # Jab tak sorted list me sahi jagah nahi milti
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Step 5: curr node ko beech me ghusa do
            curr.next = prev.next
            prev.next = curr

            # Step 6: Ab curr ko aage le jao unsorted list me
            curr = next_temp

        # Final sorted list dummy ke next me hai
        return dummy.next
