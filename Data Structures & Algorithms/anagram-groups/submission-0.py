from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            chars = [0] * 26
            for s in str:
                c = ord(s)-ord('a')
                chars[c] += 1
            groups[tuple(chars)].append(str)
        result = []
        for key in groups.keys():
            result.append(groups[key])
        return result
