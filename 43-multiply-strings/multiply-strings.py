class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1 = i + j
                p2 = i + j + 1

                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        res = ""
        for num in result:
            if not (len(res) == 0 and num == 0):
                res += chr(num + 48)

        return res
