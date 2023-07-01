class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long left = 1;
        long right = (long) 1e14;

        while (left < right) {
            long mid = left + (right - left) / 2;
            if (isPossible(mid, time, totalTrips)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean isPossible(long mid, int[] time, int totalTrips) {
        long total = 0;
        for (int t : time) {
            total += mid / t;
        }

        return total >= totalTrips;
    }
}
