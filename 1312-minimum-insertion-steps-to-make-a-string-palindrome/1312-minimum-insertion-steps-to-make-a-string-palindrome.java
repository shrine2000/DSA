class Solution {
    public int longestPalindromeSubseq(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length, max = 0;
        int[] dp = new int[n];
        for(int j = 0; j < n; j++) {
            dp[j] = 1;
            int prevMax = 0;
            for(int i = j-1; i >= 0; i--) {
                int prevLen = dp[i];
                if(chars[i] == chars[j]) {
                    dp[i] = 2 + prevMax;
                }
                prevMax = Math.max(prevMax, prevLen);
            }
        }
        int longestPalSubseq = 0;
        for(int len: dp) {
            longestPalSubseq = Math.max(longestPalSubseq, len);
        }
        return longestPalSubseq;
    }
    
    public int minInsertions(String s) {
        int longestPalSubseq = longestPalindromeSubseq(s);
        return s.length() - longestPalSubseq;
    }
}
