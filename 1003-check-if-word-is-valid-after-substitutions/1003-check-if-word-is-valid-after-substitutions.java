class Solution {
    public boolean isValid(String s) {
        int top = 0;
        char[] stack = s.toCharArray();
        for (int i = 0; i < stack.length; i++) {
            if (stack[i] != 'c') {
                stack[top++] = stack[i];
            } else {
                if (top == 0 || stack[--top] != 'b') {
                    return false;
                }
                if (top == 0 || stack[--top] != 'a') {
                    return false;
                }
            }
        }
        return top == 0;
    }
}