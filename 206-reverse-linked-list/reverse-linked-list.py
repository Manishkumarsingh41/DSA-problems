class Solution:
    def reverseList(self, head):
        # Pehle ek variable bana rahe hain 'previous' jisme pehle kuch nahi hoga
        previous = None

        # 'current' naam ka variable banaya jo initially head node par hoga
        current = head

        # Jab tak current node exist karta hai tab tak loop chalega
        while current:
            # Pehle next node ko ek temporary variable me store kar rahe hain
            next_node = current.next

            # Ab current node ka next pointer ulta karna hai, isliye usse previous pe point karwa rahe hain
            current.next = previous

            # Phir previous ko aage badha rahe hain, ab wo current ban jaayega
            previous = current

            # Ab current ko bhi aage badha rahe hain, next node pe le jaa rahe hain
            current = next_node

        # Jab poora loop khatam ho jaayega, to previous ab last node pe hoga, jo new head banega
        return previous
