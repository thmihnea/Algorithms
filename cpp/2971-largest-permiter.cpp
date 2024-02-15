#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long sum = 0;
        long long answer = -1;

        // After sorting operation, iteratively loop over each
        // element and simply check for the n-dimensional triangle
        // inequality.
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < sum) {
                answer = sum + nums[i];
            }
            sum += nums[i];
        }

        return answer;
    }
};