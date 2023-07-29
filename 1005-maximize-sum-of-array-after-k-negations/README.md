<h2><a href="https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/">1005. Maximize Sum Of Array After K Negations</a></h2><h3>Easy</h3><hr><div><p>Given an integer array <code>nums</code> and an integer <code>k</code>, modify the array in the following way:</p>

<ul>
	<li>choose an index <code>i</code> and replace <code>nums[i]</code> with <code>-nums[i]</code>.</li>
</ul>

<p>You should apply this process exactly <code>k</code> times. You may choose the same index <code>i</code> multiple times.</p>

<p>Return <em>the largest possible sum of the array after modifying it in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,3], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose index 1 and nums becomes [4,-2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,-1,0,2], k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [2,-3,-1,5,-4], k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>
</div>


## [Solution O(n)](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/252849/C%2B%2BJava-O(n)-or-O(1))


```python


def largestSumAfterKNegations(A, K):
    cnt = [0] * 201
    res = 0

    # Count the occurrences of each number in A
    for i in A:
        cnt[i + 100] += 1

    # Flip the negative numbers using the flipping technique
    for i in range(-100, 101):
        if K > 0 and cnt[i + 100] > 0:
            k = min(K, cnt[i + 100]) if i < 0 else K % 2
            cnt[-i + 100] += k
            cnt[i + 100] -= k
            K = K - k if i < 0 else 0

    # Calculate the result by accumulating the sum of occurrences multiplied by their corresponding number
    for i in range(-100, 101):
        res += i * cnt[i + 100]

    return res


```