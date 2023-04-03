<h2><a href="https://leetcode.com/problems/boats-to-save-people/">881. Boats to Save People</a></h2><h3>Medium</h3><hr><div><p>You are given an array <code>people</code> where <code>people[i]</code> is the weight of the <code>i<sup>th</sup></code> person, and an <strong>infinite number of boats</strong> where each boat can carry a maximum weight of <code>limit</code>. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most <code>limit</code>.</p>

<p>Return <em>the minimum number of boats to carry every given person</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> people = [1,2], limit = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 boat (1, 2)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> people = [3,2,2,1], limit = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 boats (1, 2), (2) and (3)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> people = [3,5,3,4], limit = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 boats (3), (3), (4), (5)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code></li>
</ul>
</div>

## Solution

### Approach 1:

```java

  public int numRescueBoats(int[] people, int limit) {
            int result = 0;  // variable to keep track of number of boats needed
            int minWeight = Integer.MAX_VALUE;  // variable to keep track of the minimum weight among all people
            int maxWeight = Integer.MIN_VALUE;  // variable to keep track of the maximum weight among all people

            // loop through all the people to find minimum and maximum weights
            for (int p : people) {
                minWeight = Math.min(minWeight, p);
                maxWeight = Math.max(maxWeight, p);
            }

            // create an array to keep count of people with each weight, indexed by weight
            int[] count = new int[maxWeight - minWeight + 1];
            for (int p : people) {
                count[p - minWeight]++;
            }

            // set the pointers to the minimum and maximum weights
            int left = minWeight;
            int right = maxWeight;

            // while the left pointer is less than the right pointer
            while (left < right) {
                // if the sum of weights at the left and right pointers is greater than the limit,
                // we can only take the person at the right pointer and move the right pointer leftwards
                if (right + left > limit) {
                    result += count[right - minWeight];
                    count[right - minWeight] = 0;
                    while (left < right && count[right - minWeight] == 0) {
                        right--;
                    }
                } else {
                    // if the sum of weights at the left and right pointers is less than or equal to the limit,
                    // we can take both the person at the left pointer and the person at the right pointer
                    // and move both pointers towards the middle of the array
                    int minCount = Math.min(count[left - minWeight], count[right - minWeight]);
                    count[left - minWeight] -= minCount;
                    count[right - minWeight] -= minCount;
                    result += minCount;
                    while (left < right && count[right - minWeight] == 0) {
                        right--;
                    }
                    while (left < right && count[left - minWeight] == 0) {
                        left++;
                    }
                }
            }

            // if there is still a person left at the middle of the array, we add them to the last boat
            if (count[left - minWeight] > 0) {
                int d = limit / left;
                if (d == 1) result += count[left - minWeight];
                else result += (count[left - minWeight] / 2) + (count[left - minWeight] % 2);
            }

            return result;  // return the number of boats needed
        }
	
	
```
