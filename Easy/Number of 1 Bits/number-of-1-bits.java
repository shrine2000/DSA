//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int N = sc.nextInt();

            Solution ob = new Solution();
            int cnt = ob.setBits(N);
            System.out.println(cnt);
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    static int setBits(int N) {
        List<Integer> arr = new ArrayList<>();
        int n = N;
        int t = 0;

        while (n > 0) {
            if (n % 2 == 0) {
                arr.add(0);
            } else {
                arr.add(1);
            }
            n = n / 2;
        }

        for (int i : arr) {
            if (i == 1) {
                t++;
            }
        }
        return t;
    }
}