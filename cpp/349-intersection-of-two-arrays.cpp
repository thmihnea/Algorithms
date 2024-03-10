#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, bool> m1;
        for (auto i : nums1) {
            m1[i] = true;
        }
        vector<int> result = vector<int>();
        for (auto entry : nums2) {
            if (m1[entry]) {
                result.push_back(entry);
                m1[entry] = false;
            }
        }
        return result;
    }
};