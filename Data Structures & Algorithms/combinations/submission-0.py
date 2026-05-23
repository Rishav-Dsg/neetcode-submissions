class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combine(i, cur):
            if len(cur) == k:
                result.append(cur[:])
                return
            if i > n:
                return 
            cur.append(i)
            combine(i+1, cur)
            cur.pop()
            combine(i+1, cur) 
        combine(1, [])
        return result    