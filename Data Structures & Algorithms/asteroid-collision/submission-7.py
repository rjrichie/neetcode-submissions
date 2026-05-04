class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()  # top explodes, keep checking
                elif stack[-1] == -asteroid:
                    stack.pop()  # both explode
                    alive = False
                else:
                    alive = False  # current asteroid explodes

            if alive:
                stack.append(asteroid)

        return stack
                