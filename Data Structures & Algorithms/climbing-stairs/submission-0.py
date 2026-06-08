class Solution:
    def __init__(self):
        self.dp = {}
    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n < 2:
            return 1
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]