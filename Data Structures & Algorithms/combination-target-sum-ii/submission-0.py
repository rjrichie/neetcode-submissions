class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, cur, total):
            if total == target:
                if cur not in res:
                    res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j + 1, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
