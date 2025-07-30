class Solution:
    def fourSum(self, nums, target):
        # Pehle list ko sort karte hain taaki two-pointer use kar sakein
        nums.sort()
        n = len(nums)
        res = []

        # First number ke liye loop
        for i in range(n):
            # Agar same number pehle aa chuka hai to skip kar dete hain
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second number ke liye loop
            for j in range(i + 1, n):
                # Ye bhi same check hai, duplicate se bachne ke liye
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Ab two pointer lagate hain bache hue do numbers ke liye
                left = j + 1
                right = n - 1

                while left < right:
                    # Chaaro number ka sum nikalte hain
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Agar sum target ke barabar hai to answer list me daal dete hain
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Left pointer ko agla unique number pe le jaate hain
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Right pointer ko bhi piche le jaake unique number pe le jaate hain
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # Agar sum chhota hai to left aage badhaate hain
                    elif total < target:
                        left += 1

                    # Agar sum bada hai to right ko piche le jaate hain
                    else:
                        right -= 1

        # Saare combinations collect ho gaye honge, ab return karte hain
        return res
