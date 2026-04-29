from typing import List
from collections import defaultdict

class Solution:
    def get_rank_label(self, rank: int) -> str:
        hmap = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        return hmap.get(rank, str(rank + 1))

    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_score = sorted(score, reverse=True)

        score_map = {}
        for rank, val in enumerate(sorted_score):
            score_map[val] = self.get_rank_label(rank)

        result = [score_map[val] for val in score]

        return result