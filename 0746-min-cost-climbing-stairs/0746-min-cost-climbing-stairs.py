class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        # Dictionary to store computed costs for each index
        memo = {}

        # Helper function with memoization
        def min_cost(idx):
            # If the result is already memoized, return it
            if idx in memo:
                return memo[idx]
            
            if idx >= len(cost):
                return 0

            cost_starting_from_current = cost[idx] + min_cost(idx + 1)
            cost_starting_from_next = cost[idx] + min_cost(idx + 2)

            # Store the result in the memo dictionary and return
            memo[idx] = min(cost_starting_from_current, cost_starting_from_next)
            return memo[idx]

        return min(min_cost(0), min_cost(1))
