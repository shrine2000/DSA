class Solution {
    public int[] diStringMatch(String S) {
        int n = S.length();
        int low = 0;
        int high = n;
        int[] A = new int[n + 1];

        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == 'I') {
                A[i] = low;
                low++;
            } else {
                A[i] = high;
                high--;
            }
        }

        A[n] = low;

        return A;
    }
}