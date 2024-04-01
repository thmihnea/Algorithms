#include <string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int counter = 0;
        bool white_space = true;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (white_space && s[i] != ' ') {
                white_space = false;
            }
            if (!white_space && s[i] == ' ') {
                break;
            }
            if (!white_space) {
                counter++;
            }
        }
        return counter;
    }
};