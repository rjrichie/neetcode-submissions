class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(idx, cur):
            if len(cur) == k:
                result.append(cur.copy())
                return
            
            for i in range(idx, n+1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(1, [])
        return result