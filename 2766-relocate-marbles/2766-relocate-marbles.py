class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        st = set(nums)
        for i in range(len(moveFrom)):
            st.remove(moveFrom[i])
            st.add(moveTo[i])
        out = list(st)
        out.sort()
        return out