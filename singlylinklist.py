# A linked list node
class Node:

    # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to traverse and print the singly linked list
def traverseList(head):
    temp=head
    # A loop that runs till head is nullptr
    while temp is not None :
		# Printing data of current node
        print(temp.data, end=" ")
		# Moving to the next node
        temp = temp.next
    print()
    
def getLength(head):
    temp=head
    count=0
    while temp is not None:
        count=count+1
		# Moving to the next node
        temp = temp.next
    print()
    print("linklist length is ",count)

def searchData(head ,key):
    while head is not None:
        if head.data==key:
            return "Key found"
            
        head=head.next
    return "Not found"  
# Driver code
def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # Example of traversing the node and printing
    traverseList(head)
    getLength(head)
    print(searchData(head ,200))

if __name__ == "__main__":
    main()
