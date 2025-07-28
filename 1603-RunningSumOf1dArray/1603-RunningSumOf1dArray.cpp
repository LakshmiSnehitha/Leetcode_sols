// Last updated: 7/28/2025, 3:29:22 PM
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (int i=1;i<nums.size();i++)
        {
            nums[i]=nums[i]+nums[i-1];
        }
    return nums;
    }
};