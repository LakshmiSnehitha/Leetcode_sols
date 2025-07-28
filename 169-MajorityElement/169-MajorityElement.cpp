// Last updated: 7/28/2025, 3:30:16 PM
class Solution {
public:
    int majorityElement(vector<int>& nums) {
       int  n=nums.size();
       sort(nums.begin(),nums.end());
        return nums[n/2];
    }
};