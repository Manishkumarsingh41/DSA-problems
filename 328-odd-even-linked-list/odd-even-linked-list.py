class Solution:
    def oddEvenList(self, head):
        # Agar linked list khali ya ek hi node hai
        if not head or not head.next:
            return head

        # Step 1: Do pointers banana hai
        odd = head
        even = head.next
        evenHead = even  # even list ka starting node hai

        # Step 2: Jab tak even aur even.next exist kare
        while even and even.next:
            odd.next = even.next  # odd ka agla node set karna hai
            odd = odd.next        # odd pointer ko aage le janan hai

            even.next = odd.next  # even ka agla node set karna
            even = even.next      # even pointer ko aage le jana hai

        # Step 3: Odd list ke end me even list jod dena hai
        odd.next = evenHead

        return head
