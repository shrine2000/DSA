int returnToBoundaryCount(int* nums, int numsSize) {
    int i = 0;
    int pos = 0, count = 0;

    for (i = 0; i < numsSize; i++) {
        pos = pos + nums[i];
        if (pos == 0) {
            count = count + 1;
        }
    }

    return count;
}
