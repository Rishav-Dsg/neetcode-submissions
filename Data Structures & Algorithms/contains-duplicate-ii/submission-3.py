class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            return len(nums) != len(set(nums))
        for i in range(len(nums)-k):
            window = nums[i:i+k+1]
            if len(window) != len(set(window)):
                return True
        return False 