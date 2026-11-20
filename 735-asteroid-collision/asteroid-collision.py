class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for curr in asteroids:
            if curr > 0:
                stack.append(curr)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(curr):
                    stack.pop()
                if stack and stack[-1] == abs(curr):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(curr)
        return stack