class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = 0
        arr = defaultdict(int)

        for log in logs:
            start = log[0]
            end = log[1]

            arr[start] += 1
            arr[end] -= 1

        max_pop = 0
        cur_pop = 0
        max_yr = -1

        for yr in sorted(arr.keys()):
            cur_pop += arr[yr]
            if cur_pop > max_pop:
                max_pop = cur_pop
                max_yr = yr
        return max_yr
