- ## [Maximum Sum of Two Numbers](https://www.desiqna.in/13267/microsoft-coding-oa-sde-1-may-3-2023)

You are given an integer array `nums` of size `n`. You need to pick any two numbers from the array such that their digit sum is equal. Then, you need to calculate their sum and return the maximum possible sum of the two numbers.

Implement the `maxSum` function to solve the problem.

*Note: The digit sum of a number is defined as the sum of its digits.*
### Example 1:

Input: `nums = [51, 71, 17, 42]`

Output: `93`

Explanation: Pick 51 and 42 to get a digit sum of 6 + 6 = 12. Add 51 and 42 to get 93 which is the maximum possible sum.
### Example 2:

Input: `nums = [42, 33, 60]`

Output: `102`

Explanation: Pick 42 and 60 to get a digit sum of 6 + 6 = 12. Add 42 and 60 to get 102 which is the maximum possible sum.
### Constraints: 
- `n == nums.length` 
- `2 <= n <= 10^4` 
- `1 <= nums[i] <= 10^5`