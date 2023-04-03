class Solution {
    public int[] evenOddBit(int n) {
       int i = 0, even = 0, odd = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                if (i % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
            n >>= 1; // shift bits to the right by 1
            i++;
        }

        return new int[]{even, odd};
    }
}