func singleNumber(nums []int) int {

    hashmap := make(map[int]int)
    
    for _, num := range nums {
        hashmap[num]++
    }
    
    for num, count := range hashmap {
        if count == 1 {
            return num
        }
    }
    
    return -1 
}