class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        char_freq = Counter(arr)
        min_heap = []
        for char, freq in char_freq.items():
            heapq.heappush(min_heap, (freq, char))
            res = ""
        while k > 0 and min_heap:
            freq, char = heapq.heappop(min_heap)
            if k >= freq:
                del char_freq[char]
                k -= freq
            else:
                break
        return len(char_freq.items())
