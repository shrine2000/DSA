[Master HEAP: Understanding 4 patterns where HEAP data structure is used
](https://leetcode.com/discuss/general-discussion/1127238/Master-HEAP%3A-Understanding-4-patterns-where-HEAP-data-structure-is-used)


https://leetcode.com/discuss/general-discussion/1088565/top-k-problems-sort-heap-and-quickselect


* While we often describe a heap as a binary tree, we do not explicitly implement it using a tree data structure.

* A heap is a complete binary tree.

- Root → `i`
- Parent of node `i` → `i // 2`
- Left child of node `i` → `2 * i`
- Right child of node `i` → `2 * i + 1`


### Min Heap

* Python's `heapq` is a min heap by default, so the smallest element is always at the root (`heap[0]`).
* Use it when you need quick access to the minimum element or want to maintain the top `k` largest elements.

```python
heapq.heappush(heap, x)
smallest = heapq.heappop(heap)
```

### Max Heap

* Python does not provide a max heap directly; simulate one by storing negative values.
* Use it when you need quick access to the maximum element repeatedly.

```python
heapq.heappush(heap, -x)
largest = -heapq.heappop(heap)
```
