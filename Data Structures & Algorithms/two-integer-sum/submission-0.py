class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hm:
                return [hm[difference], i]
            hm[n] = i