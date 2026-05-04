class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxAr = 0
        stack = []

        for i, height in enumerate(heights):
            startIdx = i
            while stack and stack[-1][1] > height:
                idx, hei = stack.pop()
                maxAr = max(maxAr, hei * (i - idx))
                startIdx = idx
            stack.append((startIdx, height))
        
        for i, h in stack:
            maxAr = max(maxAr, h * (len(heights) - i))
        
        return maxAr
