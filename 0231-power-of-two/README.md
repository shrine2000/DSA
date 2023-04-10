<h2><a href="https://leetcode.com/problems/power-of-two/">231. Power of Two</a></h2><h3>Easy</h3><hr><div><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?</div>

### Solution

Let's say we want to check if the number 8 is a power of two. 8 is represented in binary as 1000, which means it has only one bit set to 1, in the fourth position from the right. This indicates that 8 is indeed a power of two, specifically 2^3.

To check if 8 is a power of two using the bitwise AND operator, we perform the operation `(n & (n - 1))`, where `n` is equal to 8. So we have:

```
  1000   (8 in binary)
& 0111   (subtract 1 from 8 to get all bits below the highest bit flipped)
  -------
  0000   (the result of the bitwise AND operation)
``` 

Since the result of the bitwise AND operation is 0, we know that 8 has only one bit set to 1 and is therefore a power of two. If we tried this same operation with a number that is not a power of two, we would get a non-zero result and know that the number is not a power of two.

So in general, the expression `(n & (n - 1)) == 0` checks whether `n` has only one bit set to 1, and returns `true` if that's the case (indicating that `n` is a power of two), and `false` otherwise.
