from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo: dict = {}

        def dfs(idx, tid, bought):
            if tid == 2 or idx == len(prices):
                return 0
            
            # Check if solution has been memoised already.
            if (idx, tid, bought) in memo:
                return memo[(idx, tid, bought)]
            
            # If we previously bought but still had not
            # sold, we have a decision to make between
            # selling or skipping.
            if bought:
                sell = dfs(idx + 1, tid + 1, False) + prices[idx]
                skip = dfs(idx + 1, tid, bought)
                ret = max(sell, skip)
            # Otherwise, we may choose to buy or simply skip
            # the current stock.
            else:
                buy = dfs(idx + 1, tid, True) - prices[idx]
                skip = dfs(idx + 1, tid, bought)
                ret = max(buy, skip)
            
            # Store the data for memoisation purposes.
            memo[(idx, tid, bought)] = ret
            return ret
        
        return dfs(0, 0, False)
