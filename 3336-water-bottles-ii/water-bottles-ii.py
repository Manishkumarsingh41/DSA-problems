class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            empty += 1
            drunk += 1
            numExchange += 1

        return drunk
