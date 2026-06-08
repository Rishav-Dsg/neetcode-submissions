class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = {} # best you can do at that index
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        n = len(nums)
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return max(dp[n-1], dp[n-2])