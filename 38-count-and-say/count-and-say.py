class Solution:
    def countAndSay(self, n):
        # Agar n == 1 hai toh sidha "1" return karna hai
        if n == 1:
            return "1"

        s = "1"  # starting string hamesha "1" hoti hai
        for _ in range(n - 1):  # n-1 baar repeat karna hai process
            i = 0
            t = ""  # yaha hum nayi string banayenge
            while i < len(s):
                j = i
                # yaha par consecutive same digits count karenge
                while j < len(s) and s[j] == s[i]:
                    j += 1
                # ab nayi string me count + digit add karenge
                t += str(j - i) + s[i]
                # i ko aage badha do next group ke liye
                i = j
            # ab current string ko update kar do naye banaye hue se
            s = t
        # final answer return karange
        return s
