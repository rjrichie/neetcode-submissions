class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)      
            else:
                if not stack:
                    continue
                el = stack[-1]
                while stack and abs(asteroid) > el:
                    if stack: stack.pop()
                    el = stack[-1]
                
                if abs(asteroid) == el:
                    stack = stack[:-1]
        
        return stack
                