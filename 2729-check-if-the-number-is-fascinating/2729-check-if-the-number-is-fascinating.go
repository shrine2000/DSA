func isFascinating(n int) bool {
    
    newDigit := strconv.Itoa(n) + strconv.Itoa(2 * n) + strconv.Itoa(3 * n)
    uniqueDigits := make(map[rune]bool)
    
    for _, digit := range newDigit {
        if digit == '0' {
            return false
        }
        
        uniqueDigits[digit] = true
    }
    
    return len(uniqueDigits) == 9 && len(newDigit) == 9
}