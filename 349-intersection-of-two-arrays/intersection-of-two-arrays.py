class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        hmap = set()
        hmap.update(nums1)
        for num in nums2:
            if num in hmap:
                res.add(num)
        return list(res)