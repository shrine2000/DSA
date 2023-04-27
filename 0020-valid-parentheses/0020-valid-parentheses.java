class Solution {
    public boolean isValid(String s) {
        
        int topIndex = -1;
        char[] stack = new char[s.length()];
        
        for(char currentChar : s.toCharArray()){
            if(currentChar == '(' || currentChar == '[' || currentChar == '{') {
                stack[++topIndex] = currentChar;
            } else {
                if(topIndex >= 0 && ((stack[topIndex] == '(' && currentChar == ')') || (stack[topIndex] == '[' && currentChar == ']') || (stack[topIndex] == '{' && currentChar == '}'))) {
                    topIndex--;
                } else {
                    return false;
                }
            }
        }
        
        return topIndex == -1;                            
    }
}
