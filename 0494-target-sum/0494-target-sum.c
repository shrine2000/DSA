int findWays(int* nums, int numsSize, int target, int index, int currentSum) {
    // Base case: if all elements are considered
    if (index == numsSize) {
        // If the current sum equals the target, return 1, otherwise return 0
        return (currentSum == target) ? 1 : 0;
    }
    
    // Recursive cases: consider adding or subtracting the current element
    int ways = 0;
    // Add the current element to the sum and recurse
    ways += findWays(nums, numsSize, target, index + 1, currentSum + nums[index]);
    // Subtract the current element from the sum and recurse
    ways += findWays(nums, numsSize, target, index + 1, currentSum - nums[index]);
    
    return ways;
}

int findTargetSumWays(int* nums, int numsSize, int target) {
    // Start the recursion from the first element (index 0) with an initial sum of 0
    return findWays(nums, numsSize, target, 0, 0);
}
