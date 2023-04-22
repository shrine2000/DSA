<h2><a href="https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/">1312. Minimum Insertion Steps to Make a String Palindrome</a></h2><h3>Hard</h3><hr><div><p>Given a string <code>s</code>. In one step you can insert any character at any index of the string.</p>

<p>Return <em>the minimum number of steps</em> to make <code>s</code>&nbsp;palindrome.</p>

<p>A&nbsp;<b>Palindrome String</b>&nbsp;is one that reads the same backward as well as forward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "zzazz"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string "zzazz" is already palindrome we do not need any insertions.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "mbadm"
<strong>Output:</strong> 2
<strong>Explanation:</strong> String can be "mbdadbm" or "mdbabdm".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Inserting 5 characters the string becomes "leetcodocteel".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
</div>

## Solution

Minimum Insertion Steps to Make a String Palindrome is a classic problem in dynamic programming. Given a string s, we need to find the minimum number of insertions needed to make s a palindrome.

To solve this problem, we can use dynamic programming. We define a 2D array dp, where dp[i][j] represents the minimum number of insertions needed to make the substring s[i..j] a palindrome. The base case is when i=j, and in this case, dp[i][j]=0, because a single character is always a palindrome.

For all other cases, we can use the following recurrence relation:

-   if s[i]==s[j], then dp[i][j]=dp[i+1][j-1]
-   otherwise, dp[i][j]=min(dp[i+1][j],dp[i][j-1])+1

The first case means that if the first and last characters of the substring match, we don't need to insert any new characters, and we can simply look at the minimum number of insertions needed for the substring s[i+1..j-1] to be a palindrome.

The second case means that if the first and last characters of the substring do not match, we need to insert either the first character at the end or the last character at the beginning, to make the substring s[i..j] a palindrome. We can then choose the option that requires the minimum number of insertions.

The final answer is stored in dp[0][n-1], where n is the length of the string s.

In the dynamic programming solution for Minimum Insertion Steps to Make a String Palindrome, we use a 2D array `dp` to store the minimum number of insertions needed for each substring of `s` to be a palindrome.

The line `dp[i][j] = Math.min(dp[i + 1][j], dp[i][j - 1]) + 1` calculates the minimum number of insertions needed for the substring `s[i..j]` to be a palindrome, given that the first and last characters of the substring do not match.

There are two possible ways to make the substring `s[i..j]` a palindrome in this case:

1.  Insert the character `s[j]` before the character `s[i]`, and then make the substring `s[i+1..j-1]` a palindrome. The number of insertions needed for this option is `dp[i+1][j]`.
    
2.  Insert the character `s[i]` after the character `s[j]`, and then make the substring `s[i+1..j-1]` a palindrome. The number of insertions needed for this option is `dp[i][j-1]`.
    

We want to choose the option that requires the minimum number of insertions. Therefore, we take the minimum of `dp[i+1][j]` and `dp[i][j-1]`, and then add 1 to account for the new character that we inserted. This gives us the formula `dp[i][j] = Math.min(dp[i + 1][j], dp[i][j - 1]) + 1`.

By using this formula for each substring `s[i..j]`, we can fill in the entire `dp` array and obtain the minimum number of insertions needed to make the entire string `s` a palindrome.

**Faster approach**

```java 

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


```
