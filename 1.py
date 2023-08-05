from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, v in enumerate(nums):
#             ret = self.two_sum(nums[i + 1:], target - v)
#             if ret != -1:
#                 return [i, i + 1 + ret]
#         return []
#
#     def two_sum(self, nums, target):
#         for i, v in enumerate(nums):
#             if v == target:
#                 return i
#         return -1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            m[target - v] = i

        for i, v in enumerate(nums):
            if v in m and i != m[v]:
                return [i, m[v]]

        return []

