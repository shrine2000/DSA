class Solution {
    fun minimumMountainRemovals(nums: IntArray): Int {
        val n = nums.size

        val lisLeft = IntArray(n) { 1 }
        val lisRight = IntArray(n) { 1 }


        for (i in 0 until n) {
            for (j in 0 until i) {
                if (nums[i] > nums[j]) {
                    lisLeft[i] = maxOf(lisLeft[i], 1 + lisLeft[j])
                }
            }
        }

        
        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo i + 1) {
                if (nums[i] > nums[j]) {
                    lisRight[i] = maxOf(lisRight[i], 1 + lisRight[j])
                }
            }
        }

        var maxMountain = 0

        for (i in 0 until n) {
            if (lisLeft[i] > 1 && lisRight[i] > 1) {
                maxMountain = maxOf(maxMountain, lisLeft[i] + lisRight[i] - 1)
            }
        }

        return if (maxMountain > 0) n - maxMountain else -1
    }
}
