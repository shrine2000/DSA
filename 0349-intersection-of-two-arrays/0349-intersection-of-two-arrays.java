class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        BitSet bst1 = new BitSet();
        for (int num : nums1) {
            bst1.set(num);
        }

        BitSet bst2 = new BitSet();
        for (int num : nums2) {
            bst2.set(num);
        }

        bst1.and(bst2);
        int[] result = new int[bst1.cardinality()]; //  returns the number of bits that are set in bst1
        int i = 0;
        for (int num = bst1.nextSetBit(0); num >= 0; num = bst1.nextSetBit(num + 1)) {
            result[i++] = num;
        }

        return result;
    }
}