class Solution {
    public int[] evenOddBit(int n) {
        int even = 0, odd = 0;

        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                if ((i & 1) == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
 
        return new int[]{even, odd};
    }
}