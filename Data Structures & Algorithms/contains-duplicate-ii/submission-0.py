class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            if (i + k) < len(nums):
                hs = set(nums[i: i + k + 1])
                if len(hs) != k + 1:
                    return True
        return False
            