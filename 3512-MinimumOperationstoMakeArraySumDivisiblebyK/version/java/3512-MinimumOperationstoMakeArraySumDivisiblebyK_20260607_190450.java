// Last updated: 6/7/2026, 7:04:50 PM
1class Solution {
2    public int[] concatWithReverse(int[] nums) {
3        int a[]= new int[nums.length];
4        for(int i=0;i<nums.length;i++){
5            a[i] = nums[nums.length-1-i];
6        }
7        int a1[]= new int[2*nums.length];
8        for(int i=0;i<nums.length;i++){
9            a1[i]= nums[i];
10        }
11        for(int i=0;i<nums.length;i++){
12            a1[nums.length+i]=a[i];
13        }
14        return a1;
15
16    }
17}