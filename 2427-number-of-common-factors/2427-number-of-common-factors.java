class Solution {
    public int commonFactors(int a, int b) {
        int count = 0;
        int N = Math.min(a, b); // Use the minimum of a and b as the upper bound of the loop
        for(int i = 1; i <= N; i++) {
            if(a % i == 0 && b % i == 0) {
                count++;
            }
        }
        return count;
    }
}
