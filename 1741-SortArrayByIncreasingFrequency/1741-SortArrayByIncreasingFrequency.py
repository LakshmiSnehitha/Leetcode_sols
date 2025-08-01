# Last updated: 8/2/2025, 12:05:58 AM
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        nums.sort(key=lambda x:(f[x],-x))
        return nums
