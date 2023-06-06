func twoSum(nums []int, target int) []int {
    cmap := make(map[int]int)
    
    for i, num := range nums {
        c := target - num
        if index, ok := cmap[c]; ok {
            return []int{index, i}
        }
        
        cmap[num] = i
    }
    
    return []int{}
}
 