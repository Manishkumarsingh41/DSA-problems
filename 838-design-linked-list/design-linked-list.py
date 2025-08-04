# Pehle ek Node class banayi jo har ek node ke value aur next pointer ko handle karegi
class Node:
    def __init__(self, val):
        self.val = val        # Value store kar rahe hain node ke andar
        self.next = None      # Next initially none hai kyunki naye node ke baad kuch bhi nahi hai

# Ab main Linked List class bana rahe hain
class MyLinkedList:
    def __init__(self):
        self.head = None      # List ka head initially empty hai
        self.size = 0         # Size bhi zero rakha, jisse index validation aasaan ho jaaye

    # Ye function index wale node ki value return karega
    def get(self, index):
        # Pehle check kar lenge ki index valid hai ya nahi
        if index < 0 or index >= self.size:
            return -1         # Agar index galat hai to -1 return karo

        curr = self.head      # List ke head se start karenge
        i = 0
        # Jab tak index nahi milta, agla node check karte jaayenge
        while curr:
            if i == index:    # Jaise hi required index mil gaya, value return kar do
                return curr.val
            curr = curr.next
            i += 1
        return -1             # Extra safety ke liye, although upar hi check kar liya tha

    # Ye method head me naya node add karta hai
    def addAtHead(self, val):
        new_node = Node(val)         # Naya node banaya
        new_node.next = self.head    # Uska next abhi ka head ban gaya
        self.head = new_node         # Head ko update kar diya naye node pe
        self.size += 1               # Size badhaya

    # Ye method tail me node add karega
    def addAtTail(self, val):
        new_node = Node(val)         # Naya node banaya
        if not self.head:
            # Agar list empty hai to wahi head ban jaayega
            self.head = new_node
        else:
            curr = self.head
            # Last tak jaake node ko end me jod dena hai
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1               # Size badhaya

    # Kisi particular index pe node add karna hai
    def addAtIndex(self, index, val):
        # Invalid index (bada) hua to kuch nahi karna
        if index < 0 or index > self.size:
            return
        
        # Agar 0 pe add karna hai to head me add kar do
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        i = 0
        # index - 1 tak jaake waha se new node insert karenge
        while curr:
            if i == index - 1:
                new_node = Node(val)
                new_node.next = curr.next  # Naya node ke baad jo tha use connect kiya
                curr.next = new_node       # Pehle wale node ke next me naya node
                self.size += 1
                return
            curr = curr.next
            i += 1

    # Kisi index wale node ko delete karna hai
    def deleteAtIndex(self, index):
        # Agar index galat hai to kuch mat karo
        if index < 0 or index >= self.size:
            return

        # Agar 0th index hai to head hata dena hai
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        i = 0
        # Index - 1 tak jao taaki uske next ko delete kar sako
        while curr and curr.next:
            if i == index - 1:
                curr.next = curr.next.next  # Delete ka kaam - uske next ko skip kar diya
                self.size -= 1
                return
            curr = curr.next
            i += 1
