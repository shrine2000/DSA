class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for atd in asteroids:
            while stack and stack[-1]  > 0 and atd < 0:
                if stack[-1] < -atd:
                    stack.pop()
                    continue
                elif stack[-1] == -atd:
                    stack.pop()
                break
            else:
                stack.append(atd)
        return stack
