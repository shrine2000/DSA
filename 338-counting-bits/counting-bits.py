class Solution:
    def countBits(self, n: int) -> List[int]:
        bitmap = {}

        def get_bit(value):
            if value in bitmap:
                return bitmap[value]

            count = 0
            while value > 0:
                count += value % 2
                value //= 2

            bitmap[value] = count
            return count

        result = []
        for i in range(n + 1):
            result.append(get_bit(i))

        return result
