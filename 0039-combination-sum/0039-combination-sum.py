class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[0, []] for _ in range(target + 1)]

        dp[0] = [1, [[]]]
        for candidate in candidates:
            for i in range(candidate, target + 1):
                 for way in dp[i - candidate][1]:
                        new_way = way + [i]
                        dp[i][1].append(way + [candidate])
                        dp[i][0] += 1
        return dp[target][1]