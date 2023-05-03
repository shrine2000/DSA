class Solution {
    public int findDuplicate(int[] nums) {
         int duplicate = 0;
        // Get the length of the input array
        int n = nums.length;
        // Create an auxiliary array to keep track of which elements have been seen before
        int[] seenBefore = new int[n + 1];
        // Iterate through the input array
        for (int i = 0; i < n; i++) {
            // Get the current element from the input array
            int current = nums[i];
            // Check if the current element has been seen before
            if (seenBefore[current] != 0) {
                // If the current element has been seen before, it is a duplicate, so set it as the value of duplicate and break out of the loop
                duplicate = current;
                break;
            }
            // Otherwise, mark the current element as seen in the auxiliary array
            seenBefore[current] = 1;
        }
        // Return the duplicate element
        return duplicate;
    }
}