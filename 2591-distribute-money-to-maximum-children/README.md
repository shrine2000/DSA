<h2><a href="https://leetcode.com/problems/distribute-money-to-maximum-children/">2591. Distribute Money to Maximum Children</a></h2><h3>Easy</h3><hr><div><p>You are given an integer <code>money</code> denoting the amount of money (in dollars) that you have and another integer <code>children</code> denoting the number of children that you must distribute the money to.</p>

<p>You have to distribute the money according to the following rules:</p>

<ul>
	<li>All money must be distributed.</li>
	<li>Everyone must receive at least <code>1</code> dollar.</li>
	<li>Nobody receives <code>4</code> dollars.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of children who may receive <strong>exactly</strong> </em><code>8</code> <em>dollars if you distribute the money according to the aforementioned rules</em>. If there is no way to distribute the money, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> money = 20, children = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> money = 16, children = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Each child can be given 8 dollars.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= money &lt;= 200</code></li>
	<li><code>2 &lt;= children &lt;= 30</code></li>
</ul>
</div>


### Solution 1

```java

class Solution {
    public int distMoney(int money, int children) {
        money = money - children;

        if (money < 0) return -1;

        if (money < 7) return 0;

        int count = money / 7;

        if (count >= children) {
            return children - (money > children * 7 ? 1 : 0);
        }
        if ((money % 7) == 3) {
            return count - (children - count > 1 ? 0 : 1);
        }

        return count;

    }
}

```

### Solution 2 


```java 

class Solution {
    public int distMoney(int money, int children) {
        // Check if there is enough money to give each child at least 1 dollar
        if (money < children) return -1;

        // Check if the money can be evenly divided among the children and each child can receive exactly 8 dollars
        if (money % 8 == 0 && money / 8 == children) return children;

        // Give money to as many children as possible, subtracting 8 dollars from the total money for each child
        int i = 0;
        for (i = 0; i < children && money - children + i >= 0; i++) {
            money = money - 8;
        }

        // If there is 4 dollars left and all children have been given money, take 8 dollars from two of the children
        if (money == -4 && i == children) return i - 2;

        // If not all children have been given money, add 8 dollars back to the total money until there is enough to give money to all children
        while (money - children + i < 0) {
            money += 8;
            i--;
        }

        // Check if all children have been given money and if so, return the number of children who received exactly 8 dollars
        // If not all children have been given money, return the number of children who did receive money
        return money > 0 && i == children ? i - 1 : i;
    }
}

```

#### Explanation

```java 

 for (i = 0; i < children && money - children + i >= 0; i++) {
     money = money - 8;
 }
	
```

The loop starts from `i = 0`, which represents the first child, and will continue until `i` reaches the number of `children` or there is not enough money left to give $8 to the remaining children.

In each iteration of the loop, the code subtracts $8 from the remaining `money`. The condition `money - children + i >= 0` checks if there is enough money left to give $8 to the current child (i.e., `i`th child).

If there isn't enough money left for the current child, the loop will exit and the remaining money will be distributed to the remaining children using a while loop.

The loop will continue until there is enough money left to give $8 to the next child or until all children have received at least $1. If there is not enough money left to give $8 to the next child, the loop will subtract $8 from the last child, and the remaining money will be returned.
