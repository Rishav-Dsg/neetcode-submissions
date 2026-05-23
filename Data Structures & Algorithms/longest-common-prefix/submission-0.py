class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorts = sorted(strs)
        first, last = sorts[0], sorts[-1]
        a, b = len(first), len(last)
        c = a if (a < b) else b
        result = ''
        for i in range(c):
            if first[i] != last[i]:
                break
            result += first[i]
        return result
