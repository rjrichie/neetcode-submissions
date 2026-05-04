class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinedArray = [(0,0)] * len(position)
        for i in range(len(position)):
            combinedArray[i] = (position[i], speed[i])
        sortedArr = sorted(combinedArray, key=lambda tup: tup[0], reverse=True)

        timeArr = []
        for pos, spe in sortedArr:
            timeArr.append((target - pos) / spe)
        
        stack = []
        for time in timeArr:
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)