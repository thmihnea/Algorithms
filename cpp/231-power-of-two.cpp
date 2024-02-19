class Solution {
public:
    bool isPowerOfTwo(int n) {
        // The idea behind this function is to first check if the
        // given integer is positive. We know that 2^x > 0, for all x in R.
        // Afterwards, think about what happens for a power of two. Take:
        // 4 = 0100, 3 = 0011
        // You can observe that performing a logical AND operation between 4 and 3
        // will return 0000. Therefore, we need that n > 0, and that the result
        // between n & (n - 1) be 0.
        return (n > 0) && !(n & n - 1);
    }
};