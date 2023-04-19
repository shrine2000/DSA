class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(c =='a') {
                stack.push(c);
            } else if (c == 'b') {
                if(stack.isEmpty() || stack.peek() != 'a') {
                    return false;
                }
                stack.pop();
                stack.push('a');
                stack.push('b');

            } else if(c=='c'){
                if(stack.size() < 2 || stack.pop() != 'b' || stack.pop() != 'a'){
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}