func findMaxConsecutiveOnes(nums []int) int {
    count := 0
    maxCount := 0
    
    for i:= 0; i < len(nums); i++ {
        if nums[i] == 1 {
            count++
            if count > maxCount {
                maxCount = count
            }
        } else {
            count = 0
        }
        
    }
    
    return maxCount
}