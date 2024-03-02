from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        left_balls = 0
        right_balls = boxes.count("1")
        left_sum = 0
        right_sum = sum(i for i, box in enumerate(boxes) if box == "1")
        for i, box in enumerate(boxes):
            ans[i] = left_sum + right_sum
            if box == "1":
                left_balls += 1
                right_balls -= 1
            left_sum += left_balls
            right_sum -= right_balls
        return ans
