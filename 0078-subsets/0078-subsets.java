class Solution {

    public static void generatePowerSet(int[] nums, int index, List<Integer> currentSet, List<List<Integer>> powerSet) {
        if (index == nums.length) {
            powerSet.add(new ArrayList<Integer>(currentSet));
            return;
        }

        // Include the current element in the subset
        currentSet.add(nums[index]);
        generatePowerSet(nums, index + 1, currentSet, powerSet);

        // Exclude the current element from the subset
        currentSet.remove(currentSet.size() - 1);
        generatePowerSet(nums, index + 1, currentSet, powerSet);
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> powerSet = new ArrayList<>();
        List<Integer> currentSet = new ArrayList<Integer>();
        generatePowerSet(nums, 0, currentSet, powerSet);
        return powerSet;
    }
}
