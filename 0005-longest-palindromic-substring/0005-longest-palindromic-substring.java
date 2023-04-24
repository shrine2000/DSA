class Solution {
    int longest_palindrome_start = -1; // the starting index of the longest palindromic substring found so far
    int longest_palindrome_length = 0; // the length of the longest palindromic substring found so far

    public String longestPalindrome(String input_string) {
        this.longest_palindrome_start = -1;
        this.longest_palindrome_length = 0;
        explore(input_string.toCharArray(), input_string.length() / 2, 0); // explore the middle character of the string
        return this.longest_palindrome_start == -1 ? null : input_string.substring(this.longest_palindrome_start, this.longest_palindrome_start + this.longest_palindrome_length); // return the longest palindromic substring found, or null if no palindromic substring is found
    }

    public void explore(char[] input_string, int center_index, int direction) {
        // Find the longest palindromic substring centered around the character at center_index
        int left_index = center_index - 1; // initialize the left pointer
        int right_index = center_index + 1; // initialize the right pointer
        while (left_index >= 0 && input_string[left_index] == input_string[center_index]) // expand to the left as long as the characters match
            left_index--;
        while (right_index < input_string.length && input_string[right_index] == input_string[center_index]) // expand to the right as long as the characters match
            right_index++;
        int palindrome_left_index = left_index; // palindrome_left_index is the left boundary of the palindrome
        int palindrome_right_index = right_index; // palindrome_right_index is the right boundary of the palindrome
        while (palindrome_left_index >= 0 && palindrome_right_index < input_string.length && input_string[palindrome_left_index] == input_string[palindrome_right_index]) { // expand in both directions as long as the characters match
            palindrome_left_index--;
            palindrome_right_index++;
        }
        palindrome_left_index++; // move the left pointer one step to the right to get the starting index of the palindrome
        if (palindrome_right_index - palindrome_left_index > longest_palindrome_length) { // if the length of the palindrome is greater than the longest palindrome found so far
            // Update the longest palindromic substring found so far
            this.longest_palindrome_length = palindrome_right_index - palindrome_left_index;
            this.longest_palindrome_start = palindrome_left_index;
        }
        // Recursively explore the substring to the left and right of the center character
        if (direction != 2 && 2 * (left_index + 1) > this.longest_palindrome_length) // if the substring to the left of the center character could possibly contain a longer palindrome than the longest palindrome found so far
            explore(input_string, left_index, 1);
        if (direction != 1 && 2 * (input_string.length - right_index) > this.longest_palindrome_length) // if the substring to the right of the center character could possibly contain a longer palindrome than the longest palindrome found so far
            explore(input_string, right_index, 2);
    }
}
