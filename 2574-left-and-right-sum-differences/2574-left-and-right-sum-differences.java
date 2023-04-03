class Solution {
    public int[] leftRigthDifference(int[] nums) {
        int l = 0, r = 0;
        int n = nums.length;
        int[] out = new int[n];
        for (int i = 0; i < n; i++) {
            out[i] = l;
            l += nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            out[i] = Math.abs(out[i] - r);
            r += nums[i];
        }
        return out;
    }
}