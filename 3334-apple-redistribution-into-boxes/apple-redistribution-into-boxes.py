class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        c = 0
        for cpty in capacity:
            if total_apples <= 0:
                break
            total_apples -= cpty
            c += 1
        return c
