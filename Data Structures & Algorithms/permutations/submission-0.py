class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums, cur, pick):
            if len(cur) == len(nums):
                result.append(cur[:])
                return 
            for i in range(len(nums)):
                if pick[i] == False:
                    cur.append(nums[i])
                    pick[i] = True
                    perm(nums, cur, pick)
                    cur.pop()
                    pick[i] = False
        result = []
        perm(nums, [], [False]*len(nums))
        return result
        
        
