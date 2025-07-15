class Solution:
    def reverseBits(self, n):
        bits = bin(n)[2:].zfill(32)
        reversed_bits = bits[::-1]
        return int(reversed_bits, 2)
