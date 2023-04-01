<h2><a href="https://leetcode.com/problems/di-string-match/">942. DI String Match</a></h2><h3>Easy</h3><hr><div><p>A permutation <code>perm</code> of <code>n + 1</code> integers of all the integers in the range <code>[0, n]</code> can be represented as a string <code>s</code> of length <code>n</code> where:</p>

<ul>
	<li><code>s[i] == 'I'</code> if <code>perm[i] &lt; perm[i + 1]</code>, and</li>
	<li><code>s[i] == 'D'</code> if <code>perm[i] &gt; perm[i + 1]</code>.</li>
</ul>

<p>Given a string <code>s</code>, reconstruct the permutation <code>perm</code> and return it. If there are multiple valid permutations perm, return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "IDID"
<strong>Output:</strong> [0,4,1,3,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> [0,1,2,3]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "DDI"
<strong>Output:</strong> [3,2,0,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'I'</code> or <code>'D'</code>.</li>
</ul>
</div>

​Implementation of `diStringMatch` with an example.

Suppose the input string `s` is `"IDDID"`.

-   The first line of the function `int size = s.length();` will set `n` to `5`, since the length of the string is `5`.
    
-   The next line initializes an array `arr` of length `size+1`, so `arr` will be of length `6`.
    
-   The next two lines initialize two pointers `start` and `end` to `0` and `size` respectively. `start` will represent the smallest value that can be assigned to an element of `arr`, and `end` will represent the largest value that can be assigned.
    
-   The next line creates a character array `ch` from the input string `s`. So `ch` will be `['I', 'D', 'D', 'I', 'D']`.
    
-   The for loop iterates through each character in `ch`. Here's how the values of `arr`, `start`, and `end` will change for each iteration:
    
    -   For the first character `'I'`, `start` is `0`, so we assign `0` to the first element of `arr`. Then we increment `start` to `1`.
        
         
        ```
        arr = [0, _, _, _, _, _]
        start = 1
        end = 5
        ``` 
        
    -   For the second character `'D'`, `end` is `5`, so we assign `5` to the second element of `arr`. Then we decrement `end` to `4`.
        
         
        `arr = [0, 5, _, _, _, _]
        start = 1
        end = 4` 
        
    -   For the third character `'D'`, `end` is `4`, so we assign `4` to the third element of `arr`. Then we decrement `end` to `3`.
        
         
        ```
        arr = [0, 5, 4, _, _, _]
        start = 1
        end = 3
        ``` 
        
    -   For the fourth character `'I'`, `start` is `1`, so we assign `1` to the fourth element of `arr`. Then we increment `start` to `2`.
        
         
        ```
        arr = [0, 5, 4, 1, _, _]
        start = 2
        end = 3
        ``` 
        
    -   For the fifth character `'D'`, `end` is `3`, so we assign `3` to the fifth element of `arr`. Then we decrement `end` to `2`.
        
         
        ```
        arr = [0, 5, 4, 1, 3, _]
        start = 2
        end = 2
        ``` 
        
-   After the loop completes, `start` will be equal to `end`, because they will have both been incremented and decremented the same number of times. So, we set the last element of `arr` to `start`.
    
    `arr = [0, 5, 4, 1, 3, 2]` 
    
-   Finally, the function returns the array `arr`.

```java

class Solution {
    public int[] diStringMatch(String s) {
        int n = s.length();
        int[] arr = new int[n+1];
        int start = 0;
        int end = n;
        char[] ch = s.toCharArray();
        for(int i=0; i<n; i++) {
            if(ch[i] == 'I') {
                arr[i] = start++;
            } else {
                arr[i] = end--;
            }
        }
        arr[n] = start;
        return arr;
    }
}


```