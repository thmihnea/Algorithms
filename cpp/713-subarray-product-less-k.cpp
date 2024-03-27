#include <vector>

using namespace std;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0, right = 0, product = 1;
        int counter = 0;

        while (right < n) {
            product *= nums[right++];
            while (left < right && product >= k) {
                product /= nums[left++];
            }
            counter += (right - left);
        }
        return counter;
    }
};