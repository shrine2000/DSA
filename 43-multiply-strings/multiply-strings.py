class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"

        m = len(nums1)
        n = len(nums2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, - 1):
            for j in range(n -1, -1, -1):
                digit1 = ord(nums1[i]) - ord('0')
                digit2 = ord(nums2[j]) - ord('0')

                product = digit1 * digit2

                pos_low = i + j + 1
                pos_high = i + j

                total = product + res[pos_low]
                
                res[pos_low] = total % 10
                res[pos_high] += total // 10
        result_str = ''.join(map(str, res))
        return result_str.lstrip('0')
