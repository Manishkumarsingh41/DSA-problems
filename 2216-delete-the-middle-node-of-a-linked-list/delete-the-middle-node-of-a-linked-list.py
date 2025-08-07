class Solution:
    def deleteMiddle(self, head):
        # Agar list mein sirf 1 node hai, toh use delete karke None return karega
        if not head or not head.next:
            return None

        # Slow and fast pointer aur prev initialize kar rahe hain
        slow = head
        fast = head
        prev = None

        # Jab tak fast end tak nahi pahuchta, tab tak slow ek-ek step aur fast do-do step
        while fast and fast.next:
            prev = slow        # prev slow ke peechhe hoga
            slow = slow.next   # slow middle tak jaayega
            fast = fast.next.next  # fast double speed se jaayega

        # Jab loop khatam, slow middle node pe hoga
        # prev.next ko update karke middle node hata rahe hain
        prev.next = slow.next

        # Updated list ka head return karega
        return head
