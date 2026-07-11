class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap:int):
            ships, currCap = 1, cap 
            for w in weights: 
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap   #imp to reset the cap after starting a new ship
                
                currCap -= w
            return True

        while l <= r:
            cap = l + (r-l)//2 
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else :
                l = cap + 1
        return res 
