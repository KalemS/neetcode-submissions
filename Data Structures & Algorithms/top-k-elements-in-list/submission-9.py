import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        minheap = []
        for key,value in seen.items():
            heapq.heappush(minheap, (value,key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(minheap)[1])
        return result