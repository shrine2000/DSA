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
                        
        for i in range(len(dp)):
            for j in range(len(dp[i][1])):
                print("Target:", i, "Count:", dp[i][0], "Combination:", dp[i][1][j])            
            
        return dp[target][1]