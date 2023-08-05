from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        length = len(num)
        if length % 2 == 0:
            return (num[int(length / 2)] + num[int(length / 2) - 1]) / 2
        else:
            return num[int(length / 2)]