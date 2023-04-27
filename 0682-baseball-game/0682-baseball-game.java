class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        for(String string: operations){
            if(string.equals("C")){
                stack.pop();
            } else if (string.equals("D")){
                int prev  = stack.peek();
                stack.push(prev  * 2);
                
            } else if (string.equals("+")){
                int prev1 = stack.pop();
                int prev2  = stack.peek();
                stack.push(prev1);
                stack.push(prev1 + prev2);
            } else {
                stack.push(Integer.parseInt(string));
            }
        }
        
        int sum = 0;
        
        while(!stack.isEmpty()){
            sum+=stack.pop();
        }
        
        return sum;
    }
}