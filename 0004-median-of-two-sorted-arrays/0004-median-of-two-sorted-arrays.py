class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)

        if n % 2 == 1:
            return merged[n // 2]
        else:
            mid1, mid2 = n // 2 - 1, n // 2
            return (merged[mid1] + merged[mid2]) / 2.0