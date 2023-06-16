func trap(height []int) int {
    if len(height) < 3 {
        return 0;
    }
    
    left := 0
    right := len(height) - 1
    leftMax := 0
    rightMax := 0
    trappedWater := 0
    
    
    for left < right {
        if height[left] > leftMax {
            leftMax = height[left]
        }
        
        if height[right] > rightMax {
            rightMax = height[right]
        }
        
        if leftMax < rightMax {
            trappedWater += leftMax - height[left]
            left++
        } else {
            trappedWater += rightMax - height[right]
            right--
        }
    }
    
    return trappedWater 
}