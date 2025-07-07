from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nm: List[int], k: int) -> List[int]:
        """

        The `maxSlidingWindow` function solves the problem of finding the maximum value in each sliding window of size `k` within a given list `nums`. This is a classic application of the **monotonic deque (double-ended queue)** data structure, which enables maintaining window maximums efficiently in **O(n)** time, where `n` is the length of the input list. Let’s break down the approach step by step, focusing on how the deque helps maintain the maximums and why each operation is efficient.

        The function begins by checking if either `nums` is empty or `k` is zero. If so, it immediately returns an empty list, as there are no windows to process. Then, it initializes the result list `result` to collect the maximum of each window and a `deque` named `dq` to store **indices** (not values) of useful elements within the current window. The reason we store indices instead of values is that it helps track the position of elements in relation to the current window, and allows us to efficiently check and discard elements that fall outside the window range.

        The main logic runs in a single pass through the input array. For each index `i` in the list `nums`, the algorithm first checks whether the element at the front of the deque (`dq[0]`) is outside the current window. This is done by checking if the index `dq[0] < i - k + 1`. If true, that element is no longer part of the current window, so it is removed using `popleft()`. This ensures the deque always contains only indices from the current sliding window.

        Next, the algorithm ensures the deque maintains a **monotonically decreasing order** of values (not indices). This is done through a while loop that removes elements from the back of the deque (`dq.pop()`) as long as the current value `nums[i]` is greater than the value at the last index in the deque (`nums[dq[-1]]`). Why? Because any smaller value before the current one can never be a maximum in the current or future windows—it’s effectively shadowed by a larger value. Thus, these elements are purged to keep the deque clean and optimal.

        After this cleanup, the current index `i` is added to the back of the deque. By now, the front of the deque (`dq[0]`) always represents the index of the largest value in the current window. So, once the first `k` elements are processed (`i >= k - 1`), the algorithm starts recording results: it appends `nums[dq[0]]` to the `result` list, as this is the maximum of the current window.

        This process repeats until the end of the array. Because every index is pushed and popped from the deque at most once, the overall time complexity remains **O(n)**. The space complexity is **O(k)**, due to the deque holding at most `k` indices at any time.

        In summary, this solution leverages a cleverly managed deque to track potential maxima in each window. By enforcing a monotonic decreasing order and cleaning out-of-window elements, it ensures that the maximum of each window can be found in constant time, making the entire solution highly efficient and scalable for large input sizes.

        """
        a = []
        n = len(nm)
        q = deque()
        for i in range(n):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nm[q[-1]] < nm[i]:
                q.pop()
            q.append(i)

            if i >= k - 1:
                a.append(nm[q[0]])

        return a


if __name__ == "__main__":
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
