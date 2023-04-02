class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> commonElements = new ArrayList<>(); // to store the common elements
        boolean[] elementExists = new boolean[1001]; // to keep track of which elements exist in nums1

        // Iterate over the elements in nums1 and mark them as existing in the elementExists array
        for (int i = 0; i < nums1.length; i++) {
            elementExists[nums1[i]] = true;
        }

        // Iterate over the elements in nums2 and check if each exists in the elementExists array
        for (int i = 0; i < nums2.length; i++) {
            int currentElement = nums2[i];
            if (elementExists[currentElement]) { // currentElement exists in nums1
                commonElements.add(currentElement); // add currentElement to the list of common elements
                elementExists[currentElement] = false; // mark currentElement as no longer existing in nums1
            }
        }

        // Convert the ArrayList of common elements to an array of integers and return it
        int[] result = new int[commonElements.size()];
        for (int i = 0; i < commonElements.size(); i++) {
            result[i] = commonElements.get(i);
        }
        return result;
    }
}