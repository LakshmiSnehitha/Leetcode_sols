# Last updated: 7/28/2025, 3:29:52 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums=list(set(nums))
        # nums.sort()

        # if(len(nums)<3):
        #     return max(nums)
        # else:
        #     return nums[-3]
        nums=list(set(nums))
        nums.sort()
        if(len(nums)<3):
            return max(nums)
        else:
            return nums[-3]




























    #     l=[]
    #     if(len.nums==1):
    #         return nums
    #     else if(len.nums==2):
    #         return max(nums)
    #     else if(len.nums>=3):
    #         x=max(l)
    #         l.remove(x)
    #         y=max(l)
    #         l.remove(y)
    #         z=max(l)
    # return z


        
        