class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int countZeroes, countOnes, res = 0;

        // iterate through the string s
        for (int i = 0; i < s.length(); i++) {
            // reset the counts of zeroes and ones at the beginning of each iteration
            countZeroes = 0;
            countOnes = 0;
            // count the number of zeroes in the current balanced substring
            while (i < s.length() && s.charAt(i) == '0') {
                countZeroes++;
                i++;
            }
            // count the number of ones in the current balanced substring
            while (i < s.length() && s.charAt(i) == '1') {
                countOnes++;
                i++;
            }
            // compute the length of the longest balanced substring found so far
            res = Math.max(res, Math.min(countZeroes, countOnes) * 2);
            // move the pointer back to the last character of the current balanced substring
            i--;
        }
        return res;
    }
}