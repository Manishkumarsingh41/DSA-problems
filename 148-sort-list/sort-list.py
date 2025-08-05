class Solution:
    def sortList(self, head):
        # Step 1: Agar list empty hai ya sirf ek element hai toh already sorted hai
        if not head or not head.next:
            return head

        # Step 2: Saare nodes ko ek normal Python list me store kar lete hain
        nodes = []
        while head:
            nodes.append(head.val)  # har node ka value list me daal rahe
            head = head.next  # aage badh rahe

        # Step 3: Ab simple Python ka sort() use karke values ko sort kar lete hain
        nodes.sort()

        # Step 4: Ab ek naya linked list banate hain sorted values ke saath
        dummy = ListNode(0)  # dummy node banaya to help build new list
        current = dummy  # current pointer dummy par rakha

        for val in nodes:
            current.next = ListNode(val)  # naye node me value daali
            current = current.next  # current ko aage badha diya

        # Step 5: dummy.next actual sorted list ka head hoga
        return dummy.next
