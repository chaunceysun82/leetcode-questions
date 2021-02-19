class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time: O(m + n)
        # Space: O(1)

        i, j = m - 1, n - 1

        for k in range(n + m - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1