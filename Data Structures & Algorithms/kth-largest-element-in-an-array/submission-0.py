class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numToRemove = len(nums) - k
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)
        
        for i in range(numToRemove):
            heapq.heappop(heap)
        
        return heap[0]