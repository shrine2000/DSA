class Solution:
    def triangleType(self, nums: List[int]) -> str:
        def is_triangle(a, b, c):
            if a + b > c and b + c > a and c + a > b:
                return True
            else:
                return False
        
        if is_triangle(nums[0], nums[1], nums[2]):
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            if nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
                return "scalene"
            return "isosceles"
        
        return "none"
            
            
            

        