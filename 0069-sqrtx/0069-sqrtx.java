class Solution {
     public static int mySqrt(int x) {
        int left = 0;
        int right = x;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            long square = (long) middle * middle;

            if (square == x) {
                return middle;
            } else if (square < x) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return right;
    }
}