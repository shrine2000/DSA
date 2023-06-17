import (
    "sort"
)

func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    
    for _, word := range strs {
        sortedWord := sortString(word)
        groups[sortedWord] = append(groups[sortedWord], word)
        
    }
    
    result := make([][] string, 0, len(groups))
    for _, group := range groups {
        result = append(result, group)
    }
    
    
    return result
    
}

func sortString(s string) string {
    chars := []rune(s)
    
    sort.Slice(chars, func(i, j int) bool {
        return chars[i] < chars[j]
    })
    
    return string(chars)
}