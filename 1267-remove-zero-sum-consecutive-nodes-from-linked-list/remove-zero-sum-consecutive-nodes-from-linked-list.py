class Solution:
    def removeZeroSumSublists(self, head):
        # Dummy node banate hain taaki head change ho toh bhi handle kar sake
        dummy = ListNode(0)
        dummy.next = head

        prefix_sum = 0
        # Dictionary jisme prefix_sum ko last node se map karenge
        seen = {0: dummy}

        current = head
        while current:
            prefix_sum += current.val  # Ab tak ka sum calculate karte jao

            if prefix_sum in seen:
                # Agar prefix_sum pehle aa chuka hai,
                # iska matlab beech mein kuch nodes ka sum zero hai
                prev = seen[prefix_sum]  # Pehle jo node tha jahan ye sum mila tha
                node = prev.next

                temp_sum = prefix_sum
                # Ab beech ke nodes ko hataane ke liye prefix sums ko delete karenge
                while node != current:
                    temp_sum += node.val
                    if temp_sum in seen:
                        del seen[temp_sum]  # Un sums ko dict se hatao jo ab exist nahi karenge
                    node = node.next

                # Beech ke zero sum wale nodes ko skip kar do
                prev.next = current.next

            else:
                # Agar prefix_sum pehli baar aa raha hai, toh usko dict mein add karo
                seen[prefix_sum] = current

            current = current.next  # Aage badho list mein

        # Dummy.next return karenge, kyunki head change ho sakta hai
        return dummy.next
