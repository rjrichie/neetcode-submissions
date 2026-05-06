class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)      
            else:
                if not stack:
                    stack.append(asteroid)
                    continue

                el = stack[-1]
                if el < 0 and asteroid < 0:
                    stack.append(asteroid)
                    continue

                while stack and abs(asteroid) > el:
                    stack.pop()
                    el = stack[-1]
                    if el < 0:
                        break
                
                if abs(asteroid) == el:
                    stack = stack[:-1]
        
        return stack
                