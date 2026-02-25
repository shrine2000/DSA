class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = defaultdict(int)
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char in s:
                counter[char] = max(0, counter.get(char, 0) - 1)

        return bool(all([v == 0 for k, v in counter.items()]))

# check length of both strings,
# make char frequency map on string s,
# run for loop on t and reduce count of chars which are in s
# finally see if count of all chars in intial freq map is zero