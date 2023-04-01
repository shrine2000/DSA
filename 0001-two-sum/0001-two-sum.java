class Solution {
    public int[] twoSum(int[] nums, int target) {
       int n = 1;
        while (n <= nums.length - 1) {
            for (int i = 0; n + i < nums.length; i++) {
                if (nums[i] + nums[i + n] == target)
                    return new int[]{i, i + n};
            }

            n++;
        }
        return new int[]{};
    }
}