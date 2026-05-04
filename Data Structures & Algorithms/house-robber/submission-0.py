class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxL = [0] * (len(nums))
        maxL[0] = nums[0]
        maxL[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxL[i] = max(maxL[i - 1], maxL[i - 2] + nums[i])
            
        return maxL[-1]