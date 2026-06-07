// Last updated: 6/7/2026, 5:15:38 PM
1class Solution {
2    public int[] findDegrees(int[][] matrix) {
3        int ans[]= new int[matrix.length];
4
5        for(int i=0;i<matrix.length;i++){
6        int s=0;
7
8            for(int j=0;j<matrix[i].length;j++){
9                s+=matrix[i][j];
10            }
11            ans[i]=s;
12        }
13        return ans;
14    }
15}