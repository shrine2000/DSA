class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        ans = []

        while freq_map:
            for num in sorted(list(freq_map)):
                ans.append(num)
                freq_map[num] -= 1

                if freq_map[num] == 0:
                    del freq_map[num]

        return ans
