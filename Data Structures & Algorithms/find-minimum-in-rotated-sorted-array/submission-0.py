class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0 , len(nums) - 1
        minimum = nums[0]
        while i <= j:
            if nums[i] < nums[j]:
                minimum = min(minimum, nums[i])
                break

            mid = (i + j) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid - 1
        return minimum
                

