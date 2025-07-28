// Last updated: 7/28/2025, 3:30:44 PM
class Solution {
public:
    bool isValid(string s) {
        //stack;
        stack<char>st;
        for(int i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='{' ||s[i]=='['){
                st.push(s[i]);
            }
            else{
                if(s[i]==')' && !st.empty() && st.top()=='(')
                {
                    st.pop();
                }
                else if(s[i]=='}'&&!st.empty() && st.top()=='{'){
                    st.pop();
                }
                else if(s[i]==']'&&!st.empty()&& st.top()=='['){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        if(st.empty()){

            return true;
        }
        else{
            return false;
        }
        
    }
};