class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxi = max(nums)
        count = [0] * (maxi+1)
        for num in nums:
            count[num] += 1
        result = []
        for i in range(len(count)):
            result += [i] * count[i]
        nums[:] = result

            

        