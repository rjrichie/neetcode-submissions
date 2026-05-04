class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            frequency[cnt].append(num)

        arr = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                arr.append(num)
                if len(arr) == k:
                    return arr