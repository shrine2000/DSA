<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement/">424. Longest Repeating Character Replacement</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.</p>

<p>Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ABAB", k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two 'A's with two 'B's or vice versa.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "AABABBA", k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>
</div>


## Solution

**1.**
 
```java

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


```


This is a Java solution for a problem that involves finding the length of the longest substring in a string `s` that can be obtained by replacing at most `k` characters. Here's a breakdown of the code:

-   `int[] count = new int[26];` creates an integer array of size 26, which will be used to keep track of the count of each character in the current substring.
-   `int maxCount = 0;` keeps track of the maximum count of any character in the current substring.
-   `int maxLength = 0;` keeps track of the length of the longest substring that has been found so far.
-   `int left = 0;` is the index of the left end of the current substring.

The following loop goes through each character in the string `s` from left to right:

```java
for (int right = 0; right < s.length(); right++) {
    count[s.charAt(right) - 'A'] += 1;
    maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
    while (right - left + 1 - maxCount > k) {
        count[s.charAt(left) - 'A'] -= 1;
        left++;
    }
    maxLength = Math.max(maxLength, right - left + 1);
}
``` 

-   `count[s.charAt(right) - 'A'] += 1;` increments the count of the character at the current position.
-   `maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);` updates the `maxCount` if the count of the current character is greater than the current `maxCount`.
-   The `while` loop inside this `for` loop removes characters from the left end of the current substring until the difference between the length of the substring and the `maxCount` is less than or equal to `k`. This is because we want to maintain the condition that we can replace at most `k` characters in the substring. We remove characters from the left end until this condition is met.
-   `maxLength = Math.max(maxLength, right - left + 1);` updates the `maxLength` if the current substring is longer than the previous `maxLength`.

Finally, the method returns the `maxLength`, which is the length of the longest substring that can be obtained by replacing at most `k` characters.


**2.** 

```java

class Solution {
    public int characterReplacement(String s, int k) {
        if (s == null || s.length() == 0 || k < 0) {
            return 0;
        }

        if (k >= s.length()) {
            return s.length();
        }

        int[] frequency = new int[91];
        byte[] bytes = s.getBytes();
        int maxFrequency = 0;
        int start = 0;

        for (int end = 0; end < bytes.length; end++) {
            maxFrequency = Math.max(maxFrequency, ++frequency[bytes[end]]);
            while (end - start - maxFrequency + 1 > k) {
                frequency[bytes[start]]--;
                start++;
            }
        }

        return bytes.length - start;
    }
}



```
