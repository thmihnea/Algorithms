#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindromic(string& str) {
        // Retrieve the length initially as to not overuse the 
        // #size() function. Then, compute if the string is a palindrome
        // or not.
        int length = str.size();
        for (int i = 0; i < length / 2; i++) {
            if (str[i] != str[length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    string firstPalindrome(vector<string>& words) {
        // Return the first palindromic string.
        for (auto entry : words) {
            if (isPalindromic(entry)) {
                return entry;
            }
        }
        return "";
    }
};