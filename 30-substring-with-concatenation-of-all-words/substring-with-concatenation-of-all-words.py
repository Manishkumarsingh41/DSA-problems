class Solution(object):
    def findSubstring(self, s, words):
        if not words or not s:
            return []
        
        n, m, k = len(s), len(words), len(words[0])
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        result = []
        for i in range(k):
            left = right = i
            curr = {}
            count = 0
            
            while right + k <= n:
                w = s[right:right + k]
                right += k
                
                if w in word_count:
                    curr[w] = curr.get(w, 0) + 1
                    count += 1
                    
                    while curr[w] > word_count[w]:
                        lw = s[left:left + k]
                        curr[lw] -= 1
                        count -= 1
                        left += k
                    
                    if count == m:
                        result.append(left)
                else:
                    curr.clear()
                    count = 0
                    left = right
        
        return result