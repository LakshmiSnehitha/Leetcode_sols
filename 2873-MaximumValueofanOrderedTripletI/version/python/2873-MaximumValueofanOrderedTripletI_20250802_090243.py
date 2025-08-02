# Last updated: 8/2/2025, 9:02:43 AM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        s=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    s.append((nums[i]-nums[j])*nums[k])
        if(max(s)>0):
            return max(s)
        else:
            return 0