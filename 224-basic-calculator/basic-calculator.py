class Solution:
    def calculate(self, s):
        stack = []
        result = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in '+-':
                result += sign * num
                sign = 1 if char == '+' else -1
                num = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0

        return result + sign * num