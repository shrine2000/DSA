class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out = []
        for i in range(len(boxes)):
            res=0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    res+=abs(j-i)
            out.append(res)
        return out
        