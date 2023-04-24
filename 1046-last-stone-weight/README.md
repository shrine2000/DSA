<h2><a href="https://leetcode.com/problems/last-stone-weight/">1046. Last Stone Weight</a></h2><h3>Easy</h3><hr><div><p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose the <strong>heaviest two stones</strong> and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed, and</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the weight of the last remaining stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> stones = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ul>
</div>


## Solution

**1. Priority Queue**


```java 

class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones == null || stones.length == 0) {
            return 0;
        }
        
        if (stones.length == 1) {
            return stones[0];
        }
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for(int stone : stones){
            maxHeap.add(stone);
        }

        while(maxHeap.size() > 1){
            int heaviest = maxHeap.poll();
            int secondHeaviest = maxHeap.poll();
            
            if(heaviest != secondHeaviest) {
                int remaining = heaviest - secondHeaviest;
                maxHeap.add(remaining);
            }
        }
        
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}


```

This is a PriorityQueue problem because we need to keep track of the heaviest stones and always choose the two heaviest ones to smash them together.

A PriorityQueue is a data structure that provides us with a way to keep the elements sorted, and always have the smallest or largest element at the top. In this case, we want to keep the heaviest elements at the top of the priority queue so that we can easily access them and smash them together.

We also need to be able to efficiently remove elements from the middle of the priority queue and add new ones, which can be done in O(log n) time using a priority queue.

Therefore, a priority queue is a suitable data structure to solve this problem, and we can use it to keep track of the heaviest stones and repeatedly smash them together until there is at most one stone left.


**2. Bucket Sort**


```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        int maxWeight = stones[0];
        for (int stone: stones) {
            maxWeight = Math.max(maxWeight, stone);
        }
        int[] buckets = new int[maxWeight + 1];
        for (int weight : stones) {
            buckets[weight]++;
        }
        int biggestWeight = maxWeight;
        int currentWeight = maxWeight;
        while (currentWeight > 0) {
            if (buckets[currentWeight] == 0) {
                currentWeight--;
            } else if (biggestWeight == maxWeight) {
                buckets[currentWeight] %= 2;
                if (buckets[currentWeight] == 1) {
                    biggestWeight = currentWeight;
                }
                currentWeight--;
            } else {
                buckets[currentWeight]--;
                if (biggestWeight - currentWeight <= currentWeight) {
                    buckets[biggestWeight - currentWeight]++;
                    biggestWeight = maxWeight;
                } else {
                    biggestWeight -= currentWeight;
                }
            }
        }
        return biggestWeight == maxWeight ? 0 : biggestWeight;
    }
}



```

Bucket sort is a sorting algorithm that works by partitioning an array into a number of "buckets", each of which can be sorted individually using another sorting algorithm, or by recursively applying bucket sort.

In the context of the problem, we can use bucket sort to efficiently count the frequency of each stone weight in the array. This can be done by initializing an array `buckets` with length `maxWeight + 1` (where `maxWeight` is the maximum value in the `stones` array), and then incrementing the value of `buckets[stone]` for each `stone` in the `stones` array.

Once we have counted the frequency of each weight, we can iterate over the array of `buckets` to simulate the stone smashing process, as in the code you posted earlier.
