class Solution:
    def reverseBits(self, n):
        
        for i in range(16):
            j = 31 - i                      

            lower_bit = (n >> i) & 1        
            upper_bit = (n >> j) & 1        

            
            if lower_bit != upper_bit:
                n ^= (1 << i)               
                n ^= (1 << j)               

        return n