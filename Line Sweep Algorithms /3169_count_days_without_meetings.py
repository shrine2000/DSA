from typing import List


class Solution:
    @staticmethod
    def countDays(days: int, meetings: List[List[int]]) -> int:
        """
        1 2 3 4 5 6 7 8 9 10
        M M M W M M M W M M
        """
        count = [0] * days

        for meeting in meetings:
            s, e = meeting[0], meeting[1]
            for i in range(s, e + 1):
                count[i - 1] += 1
        k = 0

        for i in range(days):
            if count[i] == 0:
                k += 1

        return k


if __name__ == "__main__":
    assert Solution.countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2
