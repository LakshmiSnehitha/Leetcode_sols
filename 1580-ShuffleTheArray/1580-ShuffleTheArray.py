# Last updated: 8/4/2025, 6:44:32 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])      # x1, x2, ...
            res.append(nums[i + n])  # y1, y2, ...
        return res
