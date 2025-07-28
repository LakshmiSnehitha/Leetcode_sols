// Last updated: 7/28/2025, 3:28:49 PM
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelivin=celsius+273.15;
        double fahrenheit=celsius*1.80+32.00;
        vector<double>v;
        v.push_back(kelivin);
        v.push_back(fahrenheit);
        return v;
    }
  
};