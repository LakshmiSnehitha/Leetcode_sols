# Last updated: 8/3/2025, 5:13:56 PM
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