class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        def sub(t):
            if t == len(nums):
                result.append(temp[:])
                return 
            temp.append(nums[t])
            sub(t+1)
            temp.pop()
            sub(t+1)
        sub(0)
        return result