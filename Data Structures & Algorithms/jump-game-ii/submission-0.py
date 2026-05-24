class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            max_idx = 0

            for i in range(l, r+1):
                max_idx = max(max_idx, i+nums[i])
            l = r + 1
            r = max_idx
            result += 1
        return result