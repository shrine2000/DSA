func sortColors(nums []int) {
    zero := 0
    one := 0
    two := 0

    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            zero++
        } else if nums[i] == 1 {
            one++
        } else if nums[i] == 2 {
            two++
        }
    }

    for i := 0; i < len(nums); i++ {
        if zero != 0 {
            nums[i] = 0
            zero--
        } else if one != 0 {
            nums[i] = 1
            one--
        } else if two != 0 {
            nums[i] = 2
            two--
        }
    }
}
