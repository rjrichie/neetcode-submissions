class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        resIdx = 0

        # Look for Pivot
        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[resIdx]:
                    resIdx = l
                break


            mid = (l + r) // 2
            if nums[mid] < nums[resIdx]:
                resIdx = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        if target >= nums[0] and resIdx != 0:
            l, r = 0, resIdx - 1
        else:
            l, r = resIdx, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

        