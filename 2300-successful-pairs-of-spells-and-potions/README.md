<h2><a href="https://leetcode.com/problems/successful-pairs-of-spells-and-potions/">2300. Successful Pairs of Spells and Potions</a></h2><h3>Medium</h3><hr><div><p>You are given two positive integer arrays <code>spells</code> and <code>potions</code>, of length <code>n</code> and <code>m</code> respectively, where <code>spells[i]</code> represents the strength of the <code>i<sup>th</sup></code> spell and <code>potions[j]</code> represents the strength of the <code>j<sup>th</sup></code> potion.</p>

<p>You are also given an integer <code>success</code>. A spell and potion pair is considered <strong>successful</strong> if the <strong>product</strong> of their strengths is <strong>at least</strong> <code>success</code>.</p>

<p>Return <em>an integer array </em><code>pairs</code><em> of length </em><code>n</code><em> where </em><code>pairs[i]</code><em> is the number of <strong>potions</strong> that will form a successful pair with the </em><code>i<sup>th</sup></code><em> spell.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> spells = [5,1,3], potions = [1,2,3,4,5], success = 7
<strong>Output:</strong> [4,0,3]
<strong>Explanation:</strong>
- 0<sup>th</sup> spell: 5 * [1,2,3,4,5] = [5,<u><strong>10</strong></u>,<u><strong>15</strong></u>,<u><strong>20</strong></u>,<u><strong>25</strong></u>]. 4 pairs are successful.
- 1<sup>st</sup> spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2<sup>nd</sup> spell: 3 * [1,2,3,4,5] = [3,6,<u><strong>9</strong></u>,<u><strong>12</strong></u>,<u><strong>15</strong></u>]. 3 pairs are successful.
Thus, [4,0,3] is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> spells = [3,1,2], potions = [8,5,8], success = 16
<strong>Output:</strong> [2,0,2]
<strong>Explanation:</strong>
- 0<sup>th</sup> spell: 3 * [8,5,8] = [<u><strong>24</strong></u>,15,<u><strong>24</strong></u>]. 2 pairs are successful.
- 1<sup>st</sup> spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2<sup>nd</sup> spell: 2 * [8,5,8] = [<strong><u>16</u></strong>,10,<u><strong>16</strong></u>]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == spells.length</code></li>
	<li><code>m == potions.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= spells[i], potions[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= success &lt;= 10<sup>10</sup></code></li>
</ul>
</div>

## Solution

### Approach 1 : Prefix Sum

This solution uses counting sort to count the number of potions with a particular strength, then creates a prefix sum of these counts to allow for efficient querying of the number of potions with strength greater than or equal to a given value.

For each spell, the strength of the potion required to achieve success is computed as `success / spells[i]`. If this strength is greater than the maximum strength in the input `potions` array, then no potions can be successful for this spell and the loop moves to the next iteration. Otherwise, the loop searches for the smallest strength `target` such that `target * spells[i] >= success`. If `target` is greater than the maximum strength in the input `potions` array, then no potions can be successful for this spell and the loop moves to the next iteration. Otherwise, the solution returns the number of potions with strength greater than or equal to `target` using the prefix sum computed earlier.

Here is the Java implementation of this solution:

 
```java

class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        
        int max = -1;
        for (int x : potions)
            max = max>x?max:x;
        
        int[] potionsCount = new int[max + 1];
        for (int x : potions)
            potionsCount[x]++;
        
        int count = 0;
        for (int i = max; i >= 0; i--) {
            count += potionsCount[i];
            potionsCount[i] = count;
        }
        
        int[] ret = new int[n];
        for (int i = 0; i < n; i++) {
            long target = success / spells[i];
            if (target > max)
                continue;
            
            while (target < 100001 && target * spells[i] < success)
                target++;
            
            if (target > max)
                continue;
            
            ret[i] = potionsCount[(int)target];
        }
        
        return ret;
    }
}
```
