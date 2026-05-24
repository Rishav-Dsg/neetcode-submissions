class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 0
        for num in nums:
            length = 1
            while (num+1) in nums:
                length += 1
                num = num+1
            longest = max(longest, length)
        return longest