class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(mat)):
            hash_map[i] = mat[i].count(1)
            
        minHeap = []
        for row_id, num in hash_map.items():
            heappush(minHeap, (num, row_id))
        
        res = [heappop(minHeap)[1] for _ in range(k)]
        return res
