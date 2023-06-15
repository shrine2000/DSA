func maxSubArray(nums []int) int {
    currentMax := nums[0]
    globalMax := nums[0]
    
    for i:= 1; i < len(nums); i++ {
        currentMax = max(nums[i], currentMax + nums[i])
        globalMax = max(globalMax, currentMax)
    }
    
    return globalMax
    
}

func max(a, b int) int {
   max := a
   if b > a {
      max = b
   }
   return max
}