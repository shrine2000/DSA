class Solution {
    public int characterReplacement(String s, int k) {
        // Edge cases: if s is empty or k is negative, return 0
        if (s == null || s.length() == 0 || k < 0) {
            return 0;
        }

        // Initialize variables
        int[] count = new int[26]; // Count of each character
        int maxCount = 0; // Max count of any character in current substring
        int maxLength = 0; // Length of longest substring found
        int left = 0; // Left index of current substring

        // Loop through each character in s
        for (int right = 0; right < s.length(); right++) {
            // Increment count of character at current position
            count[s.charAt(right) - 'A']++;
            // Update maxCount
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
            
            // Check if the current substring can be made valid
            while (right - left + 1 - maxCount > k) {
                // Decrement count of character at left index
                count[s.charAt(left) - 'A']--;
                // Move left index one position to the right
                left++;
            }

            // Update maxLength
            maxLength = Math.max(maxLength, right - left + 1);
        }

        // Return the length of the longest valid substring
        return maxLength;
    }
}
