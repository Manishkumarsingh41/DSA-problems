# Node class bana rahe hain, jo har node ka value aur next pointer rakhega
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # Initially next kuch nahi

# Ab main linked list class
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)  # Dummy node banayi hai jo kabhi delete nahi hoti
        self.size = 0            # Kitne elements hain list me, track kar rahe

    # Index pe jo value hai use return karo
    def get(self, index):
        if index >= self.size:
            return -1  # Agar index invalid hai to -1 return karo

        cur = self.head.next  # Real head se start karte hain (dummy ke baad)
        for _ in range(index):
            cur = cur.next    # index tak pahuch jao
        return cur.val        # Value return karo

    # Head me naya node daalna hai
    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head.next  # Naya node ka next abhi ka head ban gaya
        self.head.next = node       # Dummy ka next ab naya node ban gaya
        self.size += 1              # Size increase kar diya

    # Tail pe naya node daalna hai
    def addAtTail(self, val):
        node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next  # Last node tak jao
        cur.next = node     # Last node ka next ab naya node ban gaya
        self.size += 1

    # Koi specific index pe node insert karna hai
    def addAtIndex(self, index, val):
        if index > self.size:
            return  # Agar index size se bada hai to kuch mat karo

        cur = self.head
        for _ in range(index):
            cur = cur.next  # index-1 tak pahuch jao

        node = ListNode(val)
        node.next = cur.next  # Naya node ka next set karo
        cur.next = node       # Pichle node ka next ab ye naya node hai
        self.size += 1

    # Index wale node ko delete karna hai
    def deleteAtIndex(self, index):
        if index >= self.size:
            return  # Invalid index to kuch nahi karna

        cur = self.head
        for _ in range(index):
            cur = cur.next  # index-1 tak jao
        cur.next = cur.next.next  # Uske next ko skip kar do, i.e., delete
        self.size -= 1
