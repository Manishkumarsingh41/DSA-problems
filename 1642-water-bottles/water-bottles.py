class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drank = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            drank += new_bottles
            empty = empty % numExchange + new_bottles
        
        return drank
        