// Last updated: 7/28/2025, 3:29:08 PM
class Solution {
    public int[] buildArray(int[] nums) {
       int arr1[]=new int[nums.length];
       for(int i=0;i<nums.length;i++)
       {
        arr1[i]=nums[nums[i]];
       } 
       return arr1;
    }
    
}