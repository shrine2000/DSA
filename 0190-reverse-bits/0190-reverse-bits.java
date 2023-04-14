public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int reversed = 0;
        for (int i = 0; i < 32; i++) {
            reversed <<= 1; // left shift by 1 bit
            reversed |= (n & 1); // add the least significant bit of n to reversed
            n >>>= 1; // right shift by 1 bit
        }
        return reversed;
    }
}