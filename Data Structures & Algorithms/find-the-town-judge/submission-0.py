class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        diff = [0] * (n + 1) # Label 1 to n
        for fr, to in trust:
            diff[fr] -= 1
            diff[to] += 1
        
        for i in range(1, len(diff)):
            if diff[i] == n - 1: # eingehende Kante
                return i 
        return -1
