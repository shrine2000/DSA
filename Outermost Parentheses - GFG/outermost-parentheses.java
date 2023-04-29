//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            String s;
            s = br.readLine();

            Solution obj = new Solution();
            String res = obj.removeOuter(s);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends


class Solution {
    public static String removeOuter(String s) {
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (!stack.isEmpty()) {
                    sb.append(c);
                }
                stack.push(c);
            } else if (c == ')') {
                stack.pop();
                if (!stack.isEmpty()) {
                    sb.append(c);
                }
            }
        }
        
        return sb.toString();
    }
}
