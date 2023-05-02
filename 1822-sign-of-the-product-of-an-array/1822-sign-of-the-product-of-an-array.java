class Solution {
    public int arraySign(int[] nums) {
        int negativeCount = 0; // Initialize the count of negative numbers to 0
        for(int num : nums) {
            if(num == 0) {
                return 0; // If the element is 0, the product is 0
            } else if(num < 0) {
                negativeCount++; // Increment the count if the element is negative
            }
        }
        
        if(negativeCount % 2 == 0) {
            return 1; // Return 1 if the number of negative numbers is even
        } else {
            return -1; // Return -1 if the number of negative numbers is odd
        }
    }
}
