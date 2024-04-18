class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        target_sum = total_sum // 3
        count = 0
        _sum = 0
        for num in arr:
            _sum += num
            if _sum == target_sum:
                count += 1
                _sum = 0
            if count == 3:
                return True
            
        return False
                
            