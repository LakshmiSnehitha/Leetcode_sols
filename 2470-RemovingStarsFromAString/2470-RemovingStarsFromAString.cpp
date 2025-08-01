// Last updated: 7/28/2025, 3:28:52 PM
class Solution {
public:
    string removeStars(string s) {
        stack<char >st;
        for(int i=0;i<s.size();i++)
        {
            if(!st.empty() and s[i]=='*')
            {
                st.pop();
            }
            else
            {
                st.push(s[i]);
            }
        }
        string ans;
        while(!st.empty())
        {
            ans+=st.top();
            st.pop();
        }
        reverse(ans.begin() ,ans.end());
        return ans;
    }
};