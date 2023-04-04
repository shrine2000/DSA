<h2><a href="https://leetcode.com/problems/optimal-partition-of-string/">2405. Optimal Partition of String</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code>, partition the string into one or more <strong>substrings</strong> such that the characters in each substring are <strong>unique</strong>. That is, no letter appears in a single substring more than <strong>once</strong>.</p>

<p>Return <em>the <strong>minimum</strong> number of substrings in such a partition.</em></p>

<p>Note that each character should belong to exactly one substring in a partition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abacaba"
<strong>Output:</strong> 4
<strong>Explanation:</strong>
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "ssssss"
<strong>Output:</strong> 6
<strong>Explanation:
</strong>The only valid partition is ("s","s","s","s","s","s").
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only English lowercase letters.</li>
</ul>
</div>

## Solution

### 1: HashSet

```java 

public int partitionString(String s) {
    int count = 0;
    Set<Character> set  = new HashSet<>();
    for(char c : s.toCharArray()) {
        if(set.contains(c)) {
            count++;
            set = new HashSet<>();
            set.add(c);
        } else {
            set.add(c);
        }
    }
    if(!set.isEmpty()) count++;
    return count;
}


```

The algorithm works as follows:

1.  Initialize a count variable to 0, and a HashSet to store the characters in the current partition.
2.  Iterate through each character in the string s.
3.  If the HashSet already contains the character c, it means that we have found a partition with duplicate characters. So, we increment the count variable and start a new partition by creating a new HashSet and adding the current character c to it.
4.  If the HashSet does not contain the character c, we add it to the HashSet.
5.  After the loop, if the HashSet is not empty, it means that we have one more partition left that contains distinct characters. So, we increment the count variable.
6.  Finally, we return the count variable which represents the number of partitions.

### 2. Bit Manipulation

```java 

public int partitionString(String s) {
    int charMap = 0;
    int count = 1;
    for(char c : s.toCharArray()) {
        if((charMap & (1 << c)) != 0) {
            count++;
            charMap = 0;
        }
        charMap ^= (1 << c);
    }
    return count;
}

```


This code uses bit manipulation to solve the problem of partitioning a string into substrings with unique characters.

The variable `map` is an integer that is used as a bit mask to keep track of which characters have been encountered so far. Initially, `map` is set to 0.

The variable `count` keeps track of the number of partitions that have been created so far. Initially, `count` is set to 1 because the entire string can be considered as one partition.

The `for` loop iterates over each character in the string `s`. For each character, the code checks if it has already been encountered by using the `&` operator to perform a bitwise AND operation between `map` and a bit mask with a 1 in the position corresponding to the character's ASCII code. If the result is not 0, then the character has already been encountered, so a new partition needs to be created. In this case, `count` is incremented and `map` is reset to 0 to start tracking the characters for the new partition.

If the character has not been encountered before, the code updates the `map` bit mask by performing a bitwise XOR operation between `map` and a bit mask with a 1 in the position corresponding to the character's ASCII code.

After the loop has processed all the characters in the string, the final value of `count` is returned.
    
In the given code, bit manipulation is used to keep track of the occurrence of each character in the input string `s`.

Here's how it works:

-   A variable `map` is initialized to 0. It will be used as a bit vector to represent the occurrence of each character.
-   For each character `c` in the string, a check is made whether the bit corresponding to that character is already set in the `map` variable. This is done by checking the result of the AND operation of `map` and `(1 << c)`.
-   If the bit is already set, it means that a new partition needs to be created. The `count` variable is incremented and the `map` variable is reset to 0 to start a new partition.
-   If the bit is not set, it means that the character has not been encountered before in the current partition. The bit corresponding to the character is set in the `map` variable using the XOR operation of `map` and `(1 << c)`.

