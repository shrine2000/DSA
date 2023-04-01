class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);


        int[] count = new int[10];
        for (int i : nums1) {
            count[i]++;
        }
        for (int j : nums2) {
            count[j]++;
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] >= 2) return i;
        }
        
        return Math.min((nums1[0]*10+nums2[0]),(nums2[0]*10+nums1[0]));
    }
}