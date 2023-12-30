class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        weaker_teams = {v for _, v in edges}
        
        if len(weaker_teams) < n - 1:
            return -1  
        
        total_possible_edges = n * (n - 1) // 2
        sum_weaker_teams = sum(weaker_teams)
        return total_possible_edges - sum_weaker_teams