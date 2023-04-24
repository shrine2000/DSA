class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int start = 0; // start index of longest palindrome
        int end = 0; // end index of longest palindrome
        boolean[][] isPalindrome = new boolean[n][n];

        // iterate over all possible palindrome lengths
        for (int len = 0; len < n; len++) {
            // iterate over all possible starting indices for substring
            for (int i = 0; i + len < n; i++) {
                int j = i + len; // end index of substring
                // check if substring is a palindrome
                if (s.charAt(i) == s.charAt(j) && (len < 2 || isPalindrome[i+1][j-1])) {
                    isPalindrome[i][j] = true;
                    // update longest palindrome indices if current substring is longer
                    if (j - i > end - start) {
                        start = i;
                        end = j;
                    }
                }
            }
        }

        // return substring of input string that is longest palindrome
        return s.substring(start, end + 1);
    }
}
