class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            a = -heapq.heappop(maxHeap)
            b = -heapq.heappop(maxHeap)
            result = a - b
            if result > 0:
                heapq.heappush(maxHeap, -result)

        if len(maxHeap) == 1:
            return -maxHeap[0]
        
        return 0