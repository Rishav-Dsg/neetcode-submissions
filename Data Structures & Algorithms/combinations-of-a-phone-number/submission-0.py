class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapped = {2: 'abc', 3: 'def', 4: 'ghi', 
            5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 
            9: 'wxyz'}
        result = []
        if len(digits) == 0:
                return result
        def back(i, s):
            if len(s) == len(digits):
                result.append(s[:])
                return 
            for c in mapped[int(digits[i])]:
                back(i+1, s+c)
        back(0, "")
        return result