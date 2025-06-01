class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ocurrance = { char:idx for idx, char in enumerate(s)}
        partitions = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_ocurrance[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions




