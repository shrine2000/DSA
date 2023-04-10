class Solution {
     public boolean isPowerOfTwo(int n) {
        if (n <= 0) {  // handle negative numbers and zero
            return false;
        }
        return (n & (n - 1)) == 0;  // check if n has only one bit set to 1
    }
}