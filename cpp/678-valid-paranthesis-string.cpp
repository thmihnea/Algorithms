#include <string>

class Solution {
public:
    bool checkValidString(std::string s) {
        int left_min = 0;
        int left_max = 0;
        for (char c : s) {
            if (c == '(') {
                left_min++, left_max++;
            }
            else if (c == ')') {
                left_min--, left_max--;
            }
            else {
                left_min--, left_max++;
            }
            if (left_max < 0) {
                return false;
            }
            left_min = left_min < 0 ? 0 : left_min;
        }
        return left_min == 0;
    }
};