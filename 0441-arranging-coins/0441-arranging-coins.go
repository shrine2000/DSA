func arrangeCoins(n int) int {
    left := 0
    right := n
    
    for left <= right {
        mid := left + (right - left ) / 2
        total := mid * (mid + 1) / 2
        
        if total == n {
            return mid
        } else if total < n {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    
    return right
    
}