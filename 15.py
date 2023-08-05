from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                return []
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = v + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    return [[v, nums[l], nums[r]]]

