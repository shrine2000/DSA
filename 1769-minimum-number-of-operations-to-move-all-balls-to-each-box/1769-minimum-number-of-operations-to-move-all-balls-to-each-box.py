from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = [int(each) for each in boxes]
        ans = [0 for _ in range(n)]
        prevBall = boxes[0]
        prevMove = 0
        for i in range(1, n):
            prevMove += prevBall 
            ans[i] += prevMove
            prevBall += boxes[i]
        prevBall = boxes[-1]
        prevMove = 0
        for i in range(n-2, -1, -1):
            prevMove += prevBall
            ans[i] += prevMove
            prevBall += boxes[i]
        return ans
