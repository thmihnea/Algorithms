#include <string>
#include <climits>

class Solution {
public:
    int myAtoi(std::string s) {
        bool negative = false;
        bool setSign = false;
        long long number = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                if (setSign) break;
                else continue;
            }
            else if (s[i] == '-' || s[i] == '+') {
                if (!setSign) {
                    negative = s[i] == '-' ? true : false;
                    setSign = true;
                } else break;
            }
            else if ('0' <= s[i] && s[i] <= '9') {
                if (!setSign) setSign = true;
                number = number * 10 + (s[i] - '0');
                if (negative && -number < INT_MIN)
                    return INT_MIN;
                if (!negative && number > INT_MAX)
                    return INT_MAX;
            } else break;
        }
        return negative ? -number : number;
    }
};