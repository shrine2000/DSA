class Solution {
   public static long findTheArrayConcVal(int[] nums) {
        int left = 0, right = nums.length - 1;
        return r(nums, 0L, left, right);
    }

    public static long r(int[] nums, long val, int left, int right) {
        if (left > right) return val; // fix: check if left > right, return val
        if (left == right) return Long.parseLong(String.valueOf(nums[left])) + val; // fix: if left == right, return single element value
        String out = "";
        out += String.valueOf(nums[left]) + String.valueOf(nums[right]);

        long res = Long.parseLong(out) + val;
        return r(nums, res, left + 1, right - 1); // fix: increment left and decrement right for next iteration
    }

   
}