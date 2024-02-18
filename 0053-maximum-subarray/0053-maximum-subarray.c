#include <limits.h>

int max(int a, int b, int c) {
    return (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
}

int max_crossing_subarray(int* nums, int low, int mid, int high) {
    int left_sum = INT_MIN;
    int right_sum = INT_MIN;
    int max_left_sum = 0;
    int max_right_sum = 0;

    for (int i = mid; i >= low; i--) {
        max_left_sum += nums[i];
        if (max_left_sum > left_sum)
            left_sum = max_left_sum;
    }

    for (int i = mid + 1; i <= high; i++) {
        max_right_sum += nums[i];
        if (max_right_sum > right_sum)
            right_sum = max_right_sum;
    }

    return left_sum + right_sum;
}

int max_subarray_recursive(int* nums, int low, int high) {
    if (low == high)
        return nums[low];

    int mid = (low + high) / 2;

    int left_sum = max_subarray_recursive(nums, low, mid);
    int right_sum = max_subarray_recursive(nums, mid + 1, high);
    int crossing_sum = max_crossing_subarray(nums, low, mid, high);

    return max(left_sum, right_sum, crossing_sum);
}

int maxSubArray(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    return max_subarray_recursive(nums, 0, numsSize - 1);
}

 