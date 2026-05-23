import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = [] 
        counter = Counter(nums)
        for key, value in counter.items():
            heapq.heappush(pq, (-value, key))
        result = []
        for i in range(k):
            freq, num = heapq.heappop(pq)
            result.append(num)
        return result