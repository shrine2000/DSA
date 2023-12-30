class Solution {
    fun findNumberOfLIS(nums: IntArray): Int {
        if (nums.isEmpty()) return 0

        val n = nums.size
        val lengths = IntArray(n) { 1 }
        val counts = IntArray(n) { 1 }
        var maxLen = 1

        for (i in 1 until n) {
            for (j in 0 until i) {
                if (nums[i] > nums[j]) {
                    if (lengths[i] == lengths[j] + 1) {
                        counts[i] += counts[j]
                    } else if (lengths[i] < lengths[j] + 1) {
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    }
                }
            }
            maxLen = maxOf(maxLen, lengths[i])
        }

        var result = 0
        for (i in 0 until n) {
            if (lengths[i] == maxLen) {
                result += counts[i]
            }
        }

        return result
    }
}
