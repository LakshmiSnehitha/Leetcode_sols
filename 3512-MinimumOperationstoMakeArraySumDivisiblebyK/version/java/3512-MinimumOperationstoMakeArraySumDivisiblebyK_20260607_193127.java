// Last updated: 6/7/2026, 7:31:27 PM
1// class Solution {
2//     public int[] concatWithReverse(int[] nums) {
3//         // int a[]= new int[nums.length];
4//         // for(int i=0;i<nums.length;i++){
5//         //     a[i] = nums[nums.length-1-i];
6//         // }
7//         // int a1[]= new int[2*nums.length];
8//         // for(int i=0;i<nums.length;i++){
9//         //     a1[i]= nums[i];
10//         // }
11//         // for(int i=0;i<nums.length;i++){
12//         //     a1[nums.length+i]=a[i];
13//         // }
14//         // return a1;
15//         int n = nums.length;
16//         nums = Arrays.copyOf(nums,n+n);  
17//         int m = nums.length - 1;         
18//         for(int i = n-1; i >= 0; i--) {
19//             nums[m-i] = nums[i];
20//         }
21//         return nums;
22//     }
23// }
24
25class Solution {
26    public int[] concatWithReverse(int[] nums) {
27
28        int n = nums.length;
29        int[] result = new int[2 * n];
30
31        // Copy original array
32        for (int i = 0; i < n; i++) {
33            result[i] = nums[i];
34        }
35
36        // Two pointers for reverse part
37        int left = n;
38        int right = n - 1;
39
40        while (right >= 0) {
41            result[left] = nums[right];
42            left++;
43            right--;
44        }
45
46        return result;
47    }
48}