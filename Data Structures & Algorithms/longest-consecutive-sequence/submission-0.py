class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hm = defaultdict(int)
        for num in nums:
            if not hm[num]:
                hm[num] = hm[num - 1] + hm[num + 1] + 1
                hm[num - hm[num - 1]] = hm[num]
                hm[num + hm[num + 1]] = hm[num]
                res = max(res, hm[num])
        
        return res