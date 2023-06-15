func sortColors(nums []int) {
    low := 0
    mid := 0
    high := len(nums) - 1
    
    for mid <= high {
        switch nums[mid] {
            case 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low++
                mid++
            case 1:
                mid++
            case 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high--
        }
    }
}
