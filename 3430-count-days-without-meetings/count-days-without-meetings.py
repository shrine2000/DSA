class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        mp = defaultdict(int)

        for m in meetings:
            mp[m[0]] += 1
            mp[m[1] + 1] -= 1

        sorted_mp_keys = sorted(mp.keys())
        ans += (
            sorted_mp_keys[0] - 1
        )  # add to the answer, all the days those are available from day 1 to first meeting day

        prev_val = mp[sorted_mp_keys[0]]
        for i in range(1, len(sorted_mp_keys)):
            current_key = sorted_mp_keys[i]
            mp[current_key] += prev_val

            if current_key <= days and mp[current_key] == 0:
                end = days + 1
                if i + 1 < len(sorted_mp_keys):
                    end = sorted_mp_keys[i + 1]
                ans += end - current_key

            prev_val = mp[current_key]

        return ans
