class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0

        def recursive(teams):
            nonlocal count
            if teams <= 1:
                return

            if teams % 2 == 0:
                matches = next_round = teams // 2
            else:
                matches = (teams - 1) // 2
                next_round = (teams - 1) // 2 + 1
            count += matches
            recursive(next_round)

        recursive(n)
        return count
