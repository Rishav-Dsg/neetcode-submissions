class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def combine(t, cur, total):
            if total == target:
                result.append(cur[:])
                return 
            if t == len(nums) or total > target:
                return 
            cur.append(nums[t])
            combine(t, cur, total+nums[t])
            cur.pop()
            combine(t+1, cur, total)
        combine(0, [], 0)
        return result