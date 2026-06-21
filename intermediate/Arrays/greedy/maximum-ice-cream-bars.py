# 1833 - Maximum Ice Cream Bars - Medium


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxCost = 0
        for cost in costs:
            maxCost = max(maxCost,cost)
        
        freq = [0] * (maxCost+1)

        for cost in costs:
            freq[cost] += 1
        
        ans = 0 
        for price in range(1,maxCost + 1):
            if freq[price] == 0:
                continue
            
            canBuy = min(freq[price], coins//price)

            coins -= canBuy *  price

            ans += canBuy

            if coins < price:
                break
        
        return ans 
