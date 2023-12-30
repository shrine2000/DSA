```
class Solution:
def canJump(self, nums: List[int]) -> bool:
memo = {}
def cj(idx, nums) -> bool:
if idx == (len(nums) - 1):
return True
if idx in memo:
return memo[idx]
for i in range(1, nums[idx] + 1):
t = idx + i
if cj(t, nums):
return True
memo[idx] = False
return False
return cj(0, nums)
```