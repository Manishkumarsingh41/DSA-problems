class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # Dekhte hain, sab numbers pehle se same hain kya?
        first_element = nums[0]

        # Array ke har number ko check karte hain.
        for element in nums:
            # Agar koi bhi number pehle number se alag mila...
            if element != first_element:
                # Toh bas ek operation lagega. Kaam khatam.
                return 1

        # Agar poora loop chal gaya aur sab same nikle,
        # toh 0 operations lagenge.
        return 0