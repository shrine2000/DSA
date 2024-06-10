from typing import List


# https://www.youtube.com/watch?v=ku4oITayEmk


class Solution:
    # Approach 1: Brute Force
    # Approach 2: This approach utilizes extra space to store the products of elements to the left and right of each element in the array.
    #             It first calculates the product of elements to the left of each element and then calculates the product of elements to the right of each element.
    #             Finally, it multiplies these two products to get the result.
    #               - Time Complexity (T.C): O(n) - It requires two passes through the array.
    #               - Space Complexity (S.C): O(n) - It uses two additional arrays of size n to store left and right products.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        output = [1] * n

        # Calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # Calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # Multiply the left and right products to get the final result
        for i in range(n):
            output[i] = left_product[i] * right_product[i]

        return output


def run_tests():
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4]
    # Expected output: [24, 12, 8, 6]
    assert solution.productExceptSelf(nums1) == [24, 12, 8, 6]

    # Test Case 2
    nums2 = [2, 4, 6, 8]
    # Expected output: [192, 96, 64, 48]
    assert solution.productExceptSelf(nums2) == [192, 96, 64, 48]

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    # Expected output: [1, 1, 1, 1, 1]
    assert solution.productExceptSelf(nums3) == [1, 1, 1, 1, 1]

    # Test Case 4
    nums4 = [0, 1, 2, 3]
    # Expected output: [6, 0, 0, 0]
    assert solution.productExceptSelf(nums4) == [6, 0, 0, 0]

    # Test Case 5
    nums5 = [-1, 2, -3, 4, -5]
    # Expected output: [120, -60, 40, -30, 24]
    assert solution.productExceptSelf(nums5) == [120, -60, 40, -30, 24]

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
