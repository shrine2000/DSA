<h2><a href="https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/">2605. Form Smallest Number From Two Digit Arrays</a></h2><h3>Easy</h3><hr><div>Given two arrays of <strong>unique</strong> digits <code>nums1</code> and <code>nums2</code>, return <em>the <strong>smallest</strong> number that contains <strong>at least</strong> one digit from each array</em>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [4,1,3], nums2 = [5,7]
<strong>Output:</strong> 15
<strong>Explanation:</strong> The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [3,5,2,6], nums2 = [3,1,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The number 3 contains the digit 3 which exists in both arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 9</code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 9</code></li>
	<li>All digits in each array are <strong>unique</strong>.</li>
</ul>
</div>


## Solution

#### Approach 1:
```java
class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
		
	int[] count = new int[10];
        for (int i : nums1) {
            count[i]++;
        }
        
        for (int j : nums2) {
            count[j]++;
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] >= 2) return i;
        }

        return Math.min((nums1[0]*10+nums2[0]),(nums2[0]*10+nums1[0]));
    }
}

```



#### Approach 2:

```java
class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int bitmask = 0;

        for (int i : nums1) {
            bitmask |= (1 << i);
        }

        for (int j : nums2) {
            if ((bitmask & (1 << j)) != 0) {
                return j;
            }
        }

        return Math.min((nums1[0] * 10 + nums2[0]), (nums2[0] * 10 + nums1[0]));
    }
}

```
