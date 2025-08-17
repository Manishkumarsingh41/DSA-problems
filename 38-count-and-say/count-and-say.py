class Solution(object):
    def countAndSay(self, n):
        result = "1"  # base case
        
        for _ in range(1, n):  
            new_result = ""  
            i = 0
            while i < len(result):
                count = 1  # digit count start
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1  # same digit mila toh count++
                new_result += str(count) + result[i]  # count+digit add
                i += 1
            result = new_result  # update result
        
        return result
