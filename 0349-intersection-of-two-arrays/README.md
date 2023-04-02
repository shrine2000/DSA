
<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays/">349. Intersection of Two Arrays</a></h2><h3>Easy</h3><hr><div><p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>
</div>


## Solution

### Approach 1 : Bit Manipulation (No sorting)

```java

 public int[] intersection(int[] nums1, int[] nums2) {
        BitSet bst1 = new BitSet();
        for (int num : nums1) {
            bst1.set(num);
        }

        BitSet bst2 = new BitSet();
        for (int num : nums2) {
            bst2.set(num);
        }

        bst1.and(bst2);
        int[] result = new int[bst1.cardinality()]; //  returns the number of bits that are set in bst1
        int i = 0;
        for (int num = bst1.nextSetBit(0); num >= 0; num = bst1.nextSetBit(num + 1)) {
            result[i++] = num;
        }

        return result;
    }

```

Here's how the implementation works:

1.  We create two `BitSet` objects, `bst1` and `bst2`, and use a loop to add each element of `nums1` and `nums2` to the respective `BitSet`. This sets the corresponding bit in the `BitSet` to `true` for each element, indicating that the element is present in the array.
    
2.  We use the `and` method of `BitSet` to compute the intersection of `bst1` and `bst2`. This sets the bits in the result `BitSet` to `true` only if they are set in both `bst1` and `bst2`, which corresponds to the common elements between the two arrays.
    
3.  We create a new integer array `result` with length equal to the number of bits set to `true` in `bst1`, which corresponds to the number of common elements.
    
4.  We use a loop to iterate over the bits set to `true` in `bst1`, starting from index 0, and add the corresponding element to the `result` array. This effectively extracts the common elements between `nums1` and `nums2`.
    
5.  We return the `result` array.
    

Overall, this implementation is efficient and has time complexity O(m + n), where m and n are the lengths of `nums1` and `nums2`, respectively. It avoids the need to sort the arrays or use nested loops, which can be slow for large input sizes.



### Approach 2 : Binary Search

```java

public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Set<Integer> set = new HashSet<>();
        for (int num : nums2) {
            if (binarySearch(nums1, num)) {
                set.add(num);
            }
        }

        int[] result = new int[set.size()];
        int i = 0;
        for (int num : set) {
            result[i++] = num;
        }

        return result;
    }

    private boolean binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}


```


### Approach 3 : Hash Set
 
We can use a hash set to store the elements of one array, and then iterate over the other array to find the common elements. This approach has time complexity O(m + n) and requires extra space proportional to the size of one array.

Here's how the implementation works:

 

```java
public static int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> set1 = new HashSet<>();
    for (int num : nums1) {
        set1.add(num);
    }
    Set<Integer> set2 = new HashSet<>();
    for (int num : nums2) {
        set2.add(num);
    }
    set1.retainAll(set2); // retain only the elements in set1 that are also in set2
    int[] result = new int[set1.size()];
    int i = 0;
    for (int num : set1) {
        result[i++] = num;
    }
    return result;
}
``` 

### Approach 4 : Two Pointers

 
We can sort both arrays and use two pointers to find the common elements. This approach has time complexity O(m log m + n log n), where m and n are the lengths of `nums1` and `nums2`, respectively. It requires extra space proportional to the size of the common elements.

Here's how the implementation works:

```java

public static int[] intersection(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    int i = 0, j = 0;
    List<Integer> list = new ArrayList<>();
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            i++;
        } else if (nums1[i] > nums2[j]) {
            j++;
        } else {
            if (list.isEmpty() || list.get(list.size() - 1) != nums1[i]) { // avoid duplicates in the result list
                list.add(nums1[i]);
            }
            i++;
            j++;
        }
    }
    int[] result = new int[list.size()];
    for (int k = 0; k < result.length; k++) {
        result[k] = list.get(k);
    }
    return result;
}
``` 

Both of these approaches are valid solutions to the "Intersection of Two Arrays" problem and may be preferable in certain situations depending on the input size and constraints.


### Approach 5 : Boolean Array
```java


public int[] intersection(int[] nums1, int[] nums2) {
    List<Integer> commonElements = new ArrayList<>(); // to store the common elements
    boolean[] elementExists = new boolean[1001]; // to keep track of which elements exist in nums1

    // Iterate over the elements in nums1 and mark them as existing in the elementExists array
    for (int i = 0; i < nums1.length; i++) {
        elementExists[nums1[i]] = true;
    }

    // Iterate over the elements in nums2 and check if each exists in the elementExists array
    for (int i = 0; i < nums2.length; i++) {
        int currentElement = nums2[i];
        if (elementExists[currentElement]) { // currentElement exists in nums1
            commonElements.add(currentElement); // add currentElement to the list of common elements
            elementExists[currentElement] = false; // mark currentElement as no longer existing in nums1
        }
    }

    // Convert the ArrayList of common elements to an array of integers and return it
    int[] result = new int[commonElements.size()];
    for (int i = 0; i < commonElements.size(); i++) {
        result[i] = commonElements.get(i);
    }
    return result;
}

```


**Other:** 

Here are several possible approaches to the "Intersection of Two Arrays" problem:

1.  Using Bit Manipulation: This approach uses bit sets to represent the arrays and performs bitwise operations to find the common elements. This approach has a time complexity of O(m + n) and requires extra space proportional to the size of the arrays.
    
2.  Using Hash Set: This approach uses hash sets to store the elements of one array and iterates over the other array to find the common elements. This approach has a time complexity of O(m + n) and requires extra space proportional to the size of one array.
    
3.  Using Two Pointers: This approach sorts both arrays and uses two pointers to find the common elements. This approach has a time complexity of O(m log m + n log n), where m and n are the lengths of the arrays, and requires extra space proportional to the size of the common elements.
    
4.  Using Binary Search: This approach sorts one array and performs binary search on it to find the common elements in the other array. This approach has a time complexity of O(m log m + n log n), where m and n are the lengths of the arrays, and requires extra space proportional to the size of the common elements.
    
5.  Using Merge Sort: This approach merges both arrays and keeps track of the common elements as it goes. This approach has a time complexity of O(m log m + n log n), where m and n are the lengths of the arrays, and requires extra space proportional to the size of the common elements.
    
6.  Using Brute Force: This approach compares every element of one array with every element of the other array to find the common elements. This approach has a time complexity of O(m * n), where m and n are the lengths of the arrays, and does not require extra space.
    

These are some possible approaches to the "Intersection of Two Arrays" problem. The best approach depends on the size of the input and any specific constraints or requirements of the problem.
