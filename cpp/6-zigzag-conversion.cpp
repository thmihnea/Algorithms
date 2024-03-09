#include <string>

#define MATRIX_SIZE 1001

class Solution {
public:
    std::string convert(std::string s, int numRows) {
        /*
        This is a safeguard statement to automatically
        handle the case when we only require one row.
        */
        if (numRows == 1) return s;

        // Initialize required data structures.
        char matrix[MATRIX_SIZE][MATRIX_SIZE] = {};
        int counter = 0, i = 0, j = 0;
        bool goingDown = false;

        /*
        We now loop over the string, keeping track of a counter.
        This counter is essentially the position at which we currently reside.
        The statement matrix[i][j] = s[counter++] assign to position (i, j) 
        the current character. If i is 0 or at the bottom row, we must swap
        the goingDown bool, and then update i and j accordingly.
        */
        while (counter < s.length()) {
            matrix[i][j] = s[counter++];
            if (i == 0 || i == numRows - 1) {
                goingDown = !goingDown;
            }
            i += goingDown ? 1 : -1;
            j += goingDown ? 0 : 1;
        }

        std::string result;

        /*
        We now rebuild the string, using numRows and the last
        value for j as guidelines for how far we should reach
        into our matrix.
        */
        for (int a = 0; a < numRows; a++) {
            for (int b = 0; b <= j; b++) {
                if (matrix[a][b] != 0) {
                    result += matrix[a][b];
                }
            }
        }

        return result;
    }
};