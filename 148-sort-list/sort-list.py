class Solution:
    def sortList(self, head):
        # Step 1: Convert Linked List to Python list
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        # Step 2: Sort the list based on node values
        nodes.sort(key=lambda node: node.val)

        # Step 3: Reconnect nodes to form the sorted linked list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if nodes:
            nodes[-1].next = None
            return nodes[0]
        return None
