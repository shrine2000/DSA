from typing import List
import heapq


# https://leetcode.com/problems/pizza-with-3n-slices/discuss/1223688/Python-O(n-log-n)-greedy%2Bheap-strategy-with-proof-(100-30ms)


class Node:
    def __init__(self, value: int = 0, left=None, right=None, deleted: bool = False):
        self.value = value
        self.left = left
        self.right = right
        self.deleted = deleted

    # Inverted/incorrect less than to work with Python's min-heap
    def __lt__(self, other):
        return self.value > other.value


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        assert n % 3 == 0

        my_heap = []
        for value in slices:
            my_heap.append(Node(value=value))

        # Initialize circular doubly linked list
        for i in range(n):
            if i == 0:
                left = my_heap[-1]
            else:
                left = my_heap[i - 1]
            if i == n - 1:
                right = my_heap[0]
            else:
                right = my_heap[i + 1]
            my_heap[i].left = left
            my_heap[i].right = right

        heapq.heapify(my_heap)
        total = 0
        remaining_slices = n // 3
        while remaining_slices != 0:
            best_node = heapq.heappop(my_heap)
            if not best_node.deleted:
                remaining_slices -= 1
                total += best_node.value

                # Delete left and right nodes from linked list
                best_node.left.left.right = best_node
                best_node.right.right.left = best_node
                best_node.left.deleted = True
                best_node.right.deleted = True

                # Replace current value with trade-in value
                best_node.value = (
                    best_node.left.value + best_node.right.value - best_node.value
                )

                best_node.left = best_node.left.left
                best_node.right = best_node.right.right

                heapq.heappush(my_heap, best_node)

        return total
