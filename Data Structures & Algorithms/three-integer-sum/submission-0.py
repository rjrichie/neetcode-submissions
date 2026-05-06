class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        left += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return result


    #     for num in nums:
    #         list_without_num = [number for number in nums if number != num]
    #         res = self.twoSum(list_without_num, -num)
    #         if res is not None:
    #             result.append(res)
    #     return result


    # def twoSum(self, nums: List[int], target):
    #     i, j = 0, len(nums) - 1
    #     while i < j:
    #         sum = nums[i] + nums[j] 
    #         if sum == target:
    #             return [nums[i], nums[j], target]
    #         elif sum < target:
    #             i += 1
    #         else:
    #             j -= 1
    #     return None