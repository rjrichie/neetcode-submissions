class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if dict.get(num) is None:
                dict[num] = 0
            dict[num] += 1
        for k, v in dict.items():
            if v > 1:
                return True
        return False
            