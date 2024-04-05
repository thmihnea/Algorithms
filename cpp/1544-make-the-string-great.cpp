#include <string>

#define EMPTY_STRING ""

class Solution {
public:
    std::string perform(std::string s) {
        std::string result = EMPTY_STRING;
        for (int i = 0; i < s.length(); i++) {
            /*
            Loop through the entire string. If the current
            character and the next are different (case-sensitive),
            but equal (case-insensitive), then simply skip them both
            when constructing the resultant string.
            */
            if (s[i] != s[i + 1] && toupper(s[i]) == toupper(s[i + 1])) {
                i++;
            } else {
                result += s[i];
            }
        }
        return result;
    }

    std::string makeGood(std::string s) {
        std::string initial = perform(s);
        /*
        The idea is to then just call this function
        multiple times until there is no other update
        to perform on the string.
        */
        while (perform(initial) != initial)
            initial = perform(initial);
        return initial;
    }
};