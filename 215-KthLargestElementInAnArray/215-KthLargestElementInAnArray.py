# Last updated: 7/28/2025, 3:30:11 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
     n=len(nums)
     nums.sort()
     return nums[n-k]