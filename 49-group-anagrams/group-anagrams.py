from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_map = defaultdict(list)
        for value in strs:
            counter_map[''.join(sorted(value))].append(value)
        return list(counter_map.values())