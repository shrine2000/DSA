class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int bitmask = 0;

        for (int i : nums1) {
            bitmask |= (1 << i);
        }

        for (int j : nums2) {
            if ((bitmask & (1 << j)) != 0) {
                return j;
            }
        }

        return Math.min((nums1[0] * 10 + nums2[0]), (nums2[0] * 10 + nums1[0]));
    }
}