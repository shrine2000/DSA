class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int[] scores = new int[divisors.length];
        for (int num : nums) {
            for (int i = 0; i < divisors.length; i++) {
                if (num % divisors[i] == 0) {
                    scores[i]++;
                }
            }
        }
        int maxScore = 0;
        int maxDivisor = Integer.MAX_VALUE;
        for (int i = 0; i < divisors.length; i++) {
            if (scores[i] > maxScore || (scores[i] == maxScore && divisors[i] < maxDivisor)) {
                maxScore = scores[i];
                maxDivisor = divisors[i];
            }
        }
        return maxDivisor;
    }
}
