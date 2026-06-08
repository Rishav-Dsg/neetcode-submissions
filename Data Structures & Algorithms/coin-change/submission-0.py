class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt in dp:
                return dp[amt]
            res = float('inf')
            for coin in coins:
                if (amt - coin) >= 0:
                    res = min(res, 1+dfs(amt-coin))
            dp[amt] = res
            return res
        mincoins = dfs(amount)
        return -1 if mincoins == float('inf') else mincoins
