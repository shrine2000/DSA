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

    def prefix_sums(self, boxes: str) -> List[int]:
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

    def two_pass_dp(self, boxes: str) -> List[int]:
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
        for i in range(n - 2, -1, -1):
            prevMove += prevBall
            ans[i] += prevMove
            prevBall += boxes[i]
        return ans

    def simple_calculation(self, boxes: str) -> List[int]:
        boxes = [1 if box == "1" else 0 for box in boxes]
        distance = sum([i for i in range(len(boxes)) if boxes[i] == 1])
        left = boxes[0]
        right = sum(boxes) - boxes[0]
        result = [distance]
        for i in range(1, len(boxes)):
            distance += left
            distance -= right
            left += boxes[i]
            right -= boxes[i]
            result.append(distance)
        return result


if __name__ == "__main__":
    sol = Solution()

    assert sol.brute_force("110") == [1, 1, 3], "Test case 1 failed"
    assert sol.brute_force("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"

    assert sol.prefix_sums("110") == [1, 1, 3], "Test case 1 failed"
    assert sol.prefix_sums("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"

    assert sol.two_pass_dp("110") == [1, 1, 3], "Test case 1 failed"
    assert sol.two_pass_dp("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"

    assert sol.simple_calculation("110") == [1, 1, 3], "Test case 1 failed"
    assert sol.simple_calculation("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"
