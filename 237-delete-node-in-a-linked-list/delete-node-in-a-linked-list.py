class Solution:
    def deleteNode(self, node):
        # Step 1: Pehle hum current node ka data overwrite karenge
        # uske next node ke data se. Basically current node ko next node bana rahe hain.
        node.val = node.next.val

        # Step 2: Ab next pointer ko change karenge — current node ka next ko skip karke
        # uske next ke next ko point karwa denge. Isse beech ka node delete ho jaayega.
        node.next = node.next.next
