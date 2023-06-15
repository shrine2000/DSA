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


/*
The Dutch National Flag algorithm is a sorting algorithm that efficiently partitions an array into three sections: elements less than a pivot, equal to the pivot, and greater than the pivot. It achieves this by using three pointers to track the boundaries between the sections while iterating through the array in a single pass.

*/