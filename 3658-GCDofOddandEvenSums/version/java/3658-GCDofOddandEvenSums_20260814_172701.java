// Last updated: 8/14/2026, 5:27:01 PM
1class Solution {
2    public int gcdOfOddEvenSums(int n) {
3        int a= n*2;
4        int b=0;
5        int c=0;
6        for(int i=0;i<=a;i++){
7            if(i%2==0){
8                b+=i;
9            }
10            else{
11                 c+=i;
12            }
13        }
14
15        while(c!=0){
16            int t=c;
17            c=b%c;
18            b=t;
19        }
20        return b;
21
22    }
23}