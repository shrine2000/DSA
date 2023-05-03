class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<Integer> diff1 = getDifference(nums1, nums2);
        List<Integer> diff2 = getDifference(nums2, nums1);
        return Arrays.asList(diff1, diff2);
    }

    private List<Integer> getDifference(int[] arr1, int[] arr2) {
        List<Integer> difference = new ArrayList<>();
        boolean[] seen = new boolean[2001];

        for (int num : arr2) {
            seen[num + 1000] = true;
        }

        for (int num : arr1) {
            if (!seen[num + 1000]) {
                seen[num + 1000] = true;
                difference.add(num);
            }
        }
        return difference;
    }
}
