from typing import List

def count_quadruplets(nums: List[int]) -> int:
    count = 0
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if nums[i] < nums[j] < nums[k] < nums[l]:
                        count += 1
                        # print(nums[i], nums[j], nums[k], nums[l])

    return count

def main():
    nums1 = [1,3,2,4,5]
    print(count_quadruplets(nums1)) 
    
    nums2 = [1,2,3,4]
    print(count_quadruplets(nums2))

if __name__ == "__main__":
    main()
