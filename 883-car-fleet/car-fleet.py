class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)],
            reverse=True,
        )
        stack = []

        for _, time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
