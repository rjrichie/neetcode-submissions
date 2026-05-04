class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            p = int((i + j) / 2)
            if nums[p] == target:
                return p
            elif nums[p] < target:
                i, j = p + 1, j
            else:
                i, j = i, p - 1

        return -1
