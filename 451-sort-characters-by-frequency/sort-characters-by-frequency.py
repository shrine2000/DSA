class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)     
        min_heap = []
        for char, freq in char_freq.items():
            heapq.heappush(min_heap, (-freq, char))
            res = ""
        while min_heap:
            freq, char  = heapq.heappop(min_heap)
            res += (char * abs(freq))
        return res