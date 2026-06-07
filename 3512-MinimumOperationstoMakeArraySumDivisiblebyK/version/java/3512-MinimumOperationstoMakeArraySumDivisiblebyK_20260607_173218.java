// Last updated: 6/7/2026, 5:32:18 PM
1class Solution {
2    public int minOperations(int[] nums, int k) {
3        int s=0;
4        for(int i=0;i<nums.length;i++){
5            s+=nums[i];
6        }
7        return s%k;
8    }
9}