// Last updated: 8/14/2026, 3:47:37 PM
1class Solution {
2    public int mirrorDistance(int n) {
3        int a=n;
4        int rev=0;
5        while(a>0){
6           int r=a%10;
7          rev=rev*10+r;
8            a=a/10;
9        }
10        return Math.abs(n-rev);
11    }
12}