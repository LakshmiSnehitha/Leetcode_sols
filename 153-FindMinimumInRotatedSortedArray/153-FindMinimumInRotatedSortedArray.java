// Last updated: 7/28/2025, 3:30:21 PM
class Solution {
    public int findMin(int[] nums) {
        int min=nums[0],i;
        for(i=1;i<=nums.length-1;i++)
        {
            if(nums[i]<min)
               min=nums[i];
        }
        return min;
    }
}