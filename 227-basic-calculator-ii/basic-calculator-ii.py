class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        s += '+'

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num) if prev * num >= 0 else -(-prev // num))
                num = 0
                sign = ch
            elif ch == ' ':
                continue

        return sum(stack)
