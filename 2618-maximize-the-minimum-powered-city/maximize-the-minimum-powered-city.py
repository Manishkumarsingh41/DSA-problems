class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        best = min(stations)
        left,right = 0,10**12
        
        while left<=right:
            mid = (left+right)//2
            
            if self.isPossible(mid,stations[:],r,k):
                left = mid+1
                best = mid
            else:
                right = mid - 1
        return best
    
    def isPossible(self,min_power,stations,r,k):
        cur_power = 0
        for i in range(r+1):
            cur_power += stations[i]
        
        left,right = 0,r
        for i in range(0,len(stations)):
            if i-left>r:
                cur_power -= stations[left]
                left+=1
            if right-i<r and right<len(stations)-1:
                right+=1
                cur_power += stations[right]
                
            if cur_power < min_power:
                power_needed = min_power-cur_power
                if k<power_needed: return False
                stations[right] += power_needed
                cur_power += power_needed
                k-=power_needed
        return True
            