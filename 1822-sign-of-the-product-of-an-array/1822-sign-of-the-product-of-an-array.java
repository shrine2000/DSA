class Solution {
    public int arraySign(int[] nums) {
        int sign = 1; // Initialize the sign to positive
        for(int num : nums) {
            if(num == 0) {
                return 0; // If the element is 0, the product is 0
            } else if(num < 0) {
                sign ^= 1; // Flip the sign bit if the element is negative
            }
        }
        return sign * 2 - 1; // Convert the sign bit to a sign (-1 or 1)
    }
}
