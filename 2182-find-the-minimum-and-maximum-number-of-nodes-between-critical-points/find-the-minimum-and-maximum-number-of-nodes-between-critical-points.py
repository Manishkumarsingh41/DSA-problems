# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        positions = []       # critical points ke positions store karenge yahan
        prev = head          # prev pointer start me head pe
        curr = head.next     # curr second node se shuru
        pos = 2              # position count second node se start (1-based indexing)

        # traverse karte hain jab tak curr aur curr.next dono exist karte hain
        while curr and curr.next:
            # check kar rahe hain ki curr node critical point hai ya nahi
            # critical point tab hota hai jab curr.val local maxima ya minima ho
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                positions.append(pos)  # position list me daal do

            prev = curr
            curr = curr.next
            pos += 1

        # agar critical points 2 se kam hain, return [-1, -1]
        if len(positions) < 2:
            return [-1, -1]

        # minimum distance nikalne ke liye start infinity se
        min_dist = float('inf')
        for i in range(1, len(positions)):
            min_dist = min(min_dist, positions[i] - positions[i-1])

        # maximum distance bas last aur first critical point ke beech ka farak
        max_dist = positions[-1] - positions[0]

        return [min_dist, max_dist]
