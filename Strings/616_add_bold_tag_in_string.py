"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

"""


class Solution:
    def add_bold_tag_in_string(self, s, dict):
        intervals = []
        for word in dict:
            index = s.find(word, 0)
            while index != -1:
                intervals.append((index, index + len(word)))
                index = s.find(word, index + 1)
        intervals.sort(key=lambda x: x[0])
        merged_intervals = self.merge_interval(intervals)

        pre = 0
        sb = []

        for st, e in merged_intervals:
            sb.append(s[pre:st])
            sb.append("<b>" + s[st:e] + "</b>")
            pre = e
        if pre < len(s):
            sb.append(s[pre:])

        return "".join(sb)

    def merge_interval(self, intervals):
        merged_intervals = []
        if not intervals:
            return merged_intervals
        merged_intervals.append(intervals[0])
        for s, e in intervals[1:]:
            if s > merged_intervals[-1][1]:
                merged_intervals.append((s, e))
            else:
                merged_intervals[-1] = (
                    merged_intervals[-1][0],
                    max(merged_intervals[-1][1], e),
                )
        return merged_intervals


if __name__ == "__main__":
    s1 = "abcxyz123"
    dict1 = ["abc", "123"]
    sol = Solution()
    assert sol.add_bold_tag_in_string(s1, dict1) == "<b>abc</b>xyz<b>123</b>"

    s2 = "aaabbcc"
    dict2 = ["aaa", "aab", "bc"]
    assert sol.add_bold_tag_in_string(s2, dict2) == "<b>aaabbc</b>c"
