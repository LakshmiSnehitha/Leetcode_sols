// Last updated: 7/28/2025, 3:29:17 PM
class Solution {
public:
    string interpret(string co) {
        string c;
        for(int i=0;i<co.size();i++)
        {
            if(co[i]=='G')
            {
                c.push_back('G');
            }
            else if(co[i]=='(' && co[i+1]==')')
            {
            c.push_back('o');
          
            }
            else if (co[i]=='(' && co[i+1]=='a' && co[i+2]=='l' && co[i+3]==')'){
                c.push_back('a');
                c.push_back('l');
            }
        } 
        return c;
    }
};