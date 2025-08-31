class Solution:
    def readBinaryWatch(self, num):
        res = []

        def backtrack(i, cnt, h, m):
            if h > 11 or m > 59:  # invalid time
                return
            if cnt == num:  # exact LEDs on -> valid time
                res.append("{}:{:02d}".format(h, m))  # add formatted time
                return
            if i == 10:  # last LED tak pahunch gaye
                return

            # LED ON
            if i < 4:  # hour LED
                backtrack(i+1, cnt+1, h | (1<<i), m)
            else:  # minute LED
                backtrack(i+1, cnt+1, h, m | (1<<(i-4)))

            # LED OFF
            backtrack(i+1, cnt, h, m)  # skip current LED

        backtrack(0, 0, 0, 0)  # start recursion from LED 0
        return res
