#include <string>

using std::string;

class Solution {
public:
    string reversePrefix(string word, char ch) {
        int index = 0;
        for (int i = 0; i < word.size(); i++)
        {
            if (word[i] == ch)
            {
                index = i;
                break;
            }
        }
        for (int i = 0; i < (index + 1) / 2; i++)
        {
            char aux = word[i];
            word[i] = word[index - i];
            word[index - i] = aux;
        }
        return word;
    }
};

        