func smallestDivisor(nums []int, threshold int) int {
    isPossible := func(mid int) bool {
        total := 0
        for _, num := range nums {
            total += int(math.Ceil(float64(num) / float64(mid)))
        }
        return total <= threshold
    }
    
    left, right := 1, getMax(nums)
    
    for left <= right {
        mid := left + (right - left) / 2
        
        if isPossible(mid) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    
    return left
}


func getMax(nums []int) int {
    max := math.MinInt32
    for _, num := range nums {
        if num > max {
            max = num
        }
    }
    return max
}