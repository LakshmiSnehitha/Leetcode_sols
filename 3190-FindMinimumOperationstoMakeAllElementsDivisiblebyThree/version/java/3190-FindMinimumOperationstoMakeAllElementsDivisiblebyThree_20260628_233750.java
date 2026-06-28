// Last updated: 6/28/2026, 11:37:50 PM
1class Solution {
2    public int minimumOperations(int[] nums) {
3        int c=0;
4        for(int i:nums){
5            if(i%3!=0){
6                c+=1;
7            }
8        }
9        return c;
10       
11    }
12}