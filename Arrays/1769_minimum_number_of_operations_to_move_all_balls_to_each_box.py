from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/discuss/1336827/Python-2-solutions-Picture-explain-Clean-and-Concise-O(N)
# https://youtube.com/watch?v=X-KSVQno6Lw&ab_channel=CodersCamp


class Solution:
    def brute_force(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(n):
            res = 0
            for j in range(n):
                if boxes[j] == "1":
                    res += abs(i - j)
            ans.append(res)
        return ans

    def dp(self, boxes: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()

    assert sol.brute_force("110") == [1, 1, 3], "Test case 1 failed"
    assert sol.brute_force("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"
