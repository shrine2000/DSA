class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(n):
            res = 0
            for j in range(n):
                if boxes[j] == '1':
                    res += abs(i - j)
            ans.append(res)
        return ans
                    