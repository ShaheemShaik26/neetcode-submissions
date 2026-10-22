class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left=0
        max_profit=0
        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                left=right
            else:
                curr_profit=prices[right]-prices[left]
                max_profit=max(max_profit,curr_profit)
        return max_profit