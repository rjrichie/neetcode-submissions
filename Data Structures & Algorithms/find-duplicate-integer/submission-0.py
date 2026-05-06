class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            targetIdx = abs(nums[idx]) - 1
            if nums[targetIdx] < 0:
                return abs(nums[targetIdx])
            nums[targetIdx] *= -1
            