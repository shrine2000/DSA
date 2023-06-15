func majorityElement(nums []int) int {
    candidate := 0
    count := 0
    
    // https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/
    
    for _, num := range nums {
        if count == 0 {
            candidate = num
        }
        if num == candidate {
            count++
        } else {
            count --
        }
    }
    
    return candidate 
}