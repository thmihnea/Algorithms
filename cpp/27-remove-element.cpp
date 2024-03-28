#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] == val) {
                for (int j = i; j < n - 1; j++) {
                    nums[j] = nums[j + 1];
                }
                nums.pop_back();
                n--; 
                i--; 
            }
        }
        return n; 
    }
};