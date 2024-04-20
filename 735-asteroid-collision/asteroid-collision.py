class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack