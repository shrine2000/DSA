### Blogs

https://leetcode.com/discuss/study-guide/2347639/a-comprehensive-guide-and-template-for-monotonic-stack-based-problems

[Monotonic Stack — Identify Pattern](https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e)

[Stack Playlist YT](https://www.youtube.com/watch?v=aiB9r8oeVp4&list=PL-Jc9J83PIiE1_SifBEWRsD-fzxrvkja9)

### Table

| **Function**             | **Stack Type**                   | **Comparison in `while` loop** | **Loop Direction** |
|--------------------------|----------------------------------|---------------------------------|--------------------|
| `next_greater_to_right`  | Decreasing (equal allowed)       | `stack[-1] <= arr[i]`           | Right to Left      |
| `next_greater_to_left`   | Decreasing (strict)              | `stack[-1] <= arr[i]`           | Left to Right      |
| `next_smaller_to_right`  | Increasing (equal allowed)       | `stack[-1] >= arr[i]`           | Right to Left      |
| `next_smaller_to_left`   | Increasing (strict)              | `stack[-1] >= arr[i]`           | Left to Right      |



### Selected Questions

1. Daily Temperatures (Medium)

2. Next Greater Element II (Medium)

3. Smallest Subsequence of Distinct Characters (Medium)

4. Trapping Rain Water (Hard)

5. Largest Rectangle in Histogram (Hard)

6. Maximal Rectangle (Hard)

7. Remove K Digits (Medium)

8. Next Greater Element I (Easy)

9. Next Greater Node In Linked List (Medium)

10. Final Prices With a Special Discount in a Shop (Easy)

11. 132 Pattern (Medium)

12. Count Submatrices With All Ones (Medium)

13. Find the Most Competitive Subsequence (Medium)

14. Sum of Subarray Minimums (Medium)

15. Maximum Subarray Min-Product (Medium)

16. Longest Well-Performing Interval (Medium)

Sentinel Value → Concept
At the end of the array, push a synthetic value that is strictly smaller than everything else.

This forces the stack to flush, popping every remaining element off the stack, hence allowing us to compute the next smaller element to the right for every unprocessed item.

https://leetcode.com/problems/sum-of-subarray-minimums/solutions/2118729/very-detailed-stack-explanation-o-n-images-comments/